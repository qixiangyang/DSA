from requests.exceptions import Timeout, ProxyError, TooManyRedirects
from lxml.html import document_fromstring, tostring
from time import localtime, strftime
from tempfile import TemporaryFile
from dataclasses import dataclass
from random import randint
from re import findall
from json import loads
from PIL import Image
from . import setting

_session = setting.get_session()


@dataclass(frozen=True)
class Article:
    url: str
    title: str
    date: str
    official_url: str
    official_name: str
    digest: str = None
    image_url: str = None

    def __getitem__(self, key):
        return getattr(self, key, None)

    def items(self):
        return [(key, value) for key, value in vars(self).items()]

    def save_article(self, save_path='.'):
        """
        保存微信文章
        :param save_path: 保存路径
        """
        html_text = _get_html(self.url)
        if html_text:
            html_tree = document_fromstring(html_text)
            title = self.title
            title = title.replace('/', '-').replace('\\', '-').replace(':', '：').replace('*', '-')
            title = title.replace('"', '”').replace('|', '-').replace('<', '-').replace('>', '-').replace('?', '？')
            with open(f'{save_path}/{title}.md', 'w', encoding='utf-8') as file:
                content_node = html_tree.xpath('//*[@id="js_content"]')[0]
                contents = [tostring(node, encoding='unicode') for node in content_node]
                text = '\n'.join(contents)
                text = text.replace(' data-', ' ')
                file.write(text)

    def get_html(self):
        """获取文章html"""
        return _get_html(self.url)


@dataclass(frozen=True)
class Official:
    url: str
    official_id: str
    name: str
    avatar_url: str
    qr_code_url: str
    profile_desc: str
    status: tuple = ()
    recent_article: Article = None
    articles: [Article] = None
    authenticate: str = None

    def __getitem__(self, key):
        return getattr(self, key, None)

    @classmethod
    def from_url(cls, url):
        """
        通过微信公众号链接实例 Official对象
        :param url: 链接
        :return: Official对象/None
        """
        domain_name = 'http://mp.weixin.qq.com'
        html_text = _get_html(url)
        if not html_text: return None  # 验证码/代理失败
        html_tree = document_fromstring(html_text)
        official_id = _extract(html_tree, '/html/body/div/div[1]/div[1]/div[1]/div/p', True)[5:]
        name = _extract(html_tree, '/html/body/div/div[1]/div[1]/div[1]/div/strong', True)
        avatar_url = _extract(html_tree, '/html/body/div/div[1]/div[1]/div[1]/span/img/@src')
        qr_code_url = domain_name + _extract(html_tree, '//*[@id="js_pc_qr_code_img"]/@src')
        profile_desc = _extract(html_tree, '/html/body/div/div[1]/div[1]/ul/li[1]/div', True)
        authenticate = _extract(html_tree, '/html/body/div/div[1]/div[1]/ul/li[2]/div', True)
        articles = []

        result = findall('var msgList = {"list":(\[.*?\])};', html_text)
        if result:
            for item in loads(result[0]):
                date = strftime('%Y-%m-%d', localtime(item['comm_msg_info']['datetime']))
                for info in item['app_msg_ext_info']['multi_app_msg_item_list']:
                    article_url = info['content_url'] if info['content_url'].startswith('http') else domain_name + info[
                        'content_url']
                    articles.append(Article(
                        url=article_url.replace('&amp;', '&'),
                        title=info['title'],
                        date=date,
                        official_url=url,
                        official_name=name,
                        digest=info['digest'],
                        image_url=info['cover'],
                    ))

        recent_article = articles[0] if articles else None
        articles = articles if articles else None
        return cls(
            url=url,
            official_id=official_id,
            name=name,
            avatar_url=avatar_url,
            qr_code_url=qr_code_url,
            profile_desc=profile_desc,
            authenticate=authenticate,
            recent_article=recent_article,
            articles=articles,
        )

    def items(self):
        return [(key, value) for key, value in vars(self).items()]


def _get_html(url):
    """
    获取页面
    :param url: 链接
    :return: html文本/None
    """
    if setting.get_proxy:
        for _ in range(setting.repeat_times):
            proxies = setting.get_proxy()
            try:
                resp = _session.get(url, proxies=proxies, timeout=setting.proxy_timeout)
            except (Timeout, ProxyError, TooManyRedirects):
                continue
            if url == resp.url:
                return str(resp.content, 'utf-8')
        else:
            resp = _session.get(url)
            if url == resp.url:
                return str(resp.content, 'utf-8')
            setting.proxy_error_callback(url)
            return None
    else:
        resp = _session.get(url)
        if '请输入验证码' in resp.text: return _get_html(url) if _identify_captcha() else None
        elif any([t in resp.text for t in ['系统出错', '链接已过期', '该内容已被发布者删除', '此内容因违规无法查看']]):
            setting.wechat_link_error_callback(url)
            return None
        else:
            return str(resp.content, 'utf-8')


def _extract(node, xpath, is_text=False):
    """
    安全提取关键信息
    :param node: [lxml.element] html节点
    :param xpath: [str] xpath规则
    :param is_text: 是否获取节点文本
    """
    result = node.xpath(xpath)
    result = result[0] if result else None
    return None if result is None else result.text_content().strip() if is_text else result


def _identify_captcha():
    """
    验证码识别
    :return: True/False
    """
    for _ in range(setting.repeat_times):
        cert = randint(100000, 999999)
        resp = _session.get(f'http://mp.weixin.qq.com/mp/verifycode?cert={cert}')
        tf = TemporaryFile()
        tf.write(resp.content)
        code = setting.wechat_captcha_callback(Image.open(tf))
        if not code:
            continue
        resp = _session.post('http://mp.weixin.qq.com/mp/verifycode', data=f'cert={cert}&input={code}&appmsg_token=""')
        resp.encoding = 'utf-8'
        msg = resp.json()
        if msg['ret'] == 0:
            return True
        print('验证码错误！')
    return False
