from requests.exceptions import Timeout, ProxyError, TooManyRedirects
from requests.utils import add_dict_to_cookiejar
from lxml.html import document_fromstring
from .wechat import Article, Official
from time import localtime, strftime
from tempfile import TemporaryFile
from urllib.parse import quote
from re import search, findall
from random import randint
from json import loads
from time import time
from PIL import Image
from . import setting

_session = setting.get_session()


def search_articles(keyword, pages=1, begin_page=1):
    """
    搜索微信文章
    :param keyword: 搜索关键字
    :param pages: 页面数
    :param begin_page: 起始页
    :return: Generator-Article对象
    """
    search_urls = [f'https://weixin.sogou.com/weixin?type=2&query={quote(keyword)}&page={page}'
                   for page in range(begin_page, begin_page + pages)]
    for search_url in search_urls:
        html_text = _get_html(search_url)
        if not html_text: continue
        article_nodes = document_fromstring(html_text).xpath('//*[@class="news-list"]/li')
        _session.headers.update({'Referer': search_url})
        for node in article_nodes:
            yield Article(
                url=_extract(node, './div[2]/h3/a/@data-share'),
                title=_extract(node, './div[2]/h3/a', True),
                date=strftime('%Y-%m-%d', localtime(int(_extract(node, './div[2]/div/@t')))),
                image_url=_extract(node, './div[1]/a/img/@src'),
                digest=_extract(node, './div[2]/p', True),
                official_url=_parse_link(_extract(node, './div[2]/div/a/@href')),
                official_name=_extract(node, './div[2]/div/a/text()'),
            )


def search_officials(keyword, pages=1, begin_page=1):
    """
    搜索微信公众号
    :param keyword: 搜索关键字
    :param pages: 页面数
    :param begin_page: 起始页
    :return: Generator-Official对象
    """
    search_urls = [f'https://weixin.sogou.com/weixin?type=1&query={quote(keyword)}&page={page}'
                   for page in range(begin_page, begin_page + pages)]
    for search_url in search_urls:
        print(search_url)
        _session.headers.update({'Referer': search_url})
        html_text = _get_html(search_url)
        # print(html_text)
        if not html_text: continue
        html_tree = document_fromstring(html_text)
        official_nodes = html_tree.xpath('//*[@id="main"]/div[4]/ul/li')
        for official_node in official_nodes:
            yield _parse_official_node(html_text, official_node)


def get_official(official_id):
    """
    获取微信公众号html_tree
    :param official_id: 微信号
    :return: Official对象/None
    """
    search_url = f'https://weixin.sogou.com/weixin?type=1&query={official_id}'
    _session.headers.update({'Referer': search_url})
    html_text = _get_html(search_url)
    if not html_text: return None
    html_tree = document_fromstring(html_text)
    official_node = html_tree.xpath('//*[@id="main"]/div[4]/ul/li[1]')
    if official_node:
        official_node = official_node[0]
        if str(official_id) == str(_extract(official_node, './div/div[2]/p[2]/label/text()')):
            return _parse_official_node(html_text, official_node)
    return None


def get_hot_articles(pages=2, article_type=0):
    """
    获取微信热门文章
    :param pages: 获取页面数量
    :param article_type: 微信文章类型
    :return: Generator-Official对象
    """
    urls = [f'https://weixin.sogou.com/pcindex/pc/pc_{article_type}/{index}.html' for index in range(1, pages + 1)]
    for url in urls:
        html_tree = document_fromstring(_get_html(url, False))
        article_nodes = html_tree.xpath('/html/body/li')
        for node in article_nodes:
            url = _extract(node, './div[1]/a/@href')
            title = _extract(node, './div[2]/h3/a', True)
            date = _extract(node, './div[2]/div/span/@t')
            date = strftime('%Y-%m-%d', localtime(int(date)))
            official_url = _extract(node, './div[2]/div/a/@href')
            official_name = _extract(node, './div[2]/div/a', True)
            digest = _extract(node, './div[2]/p', True)
            image_url = _extract(node, './div[1]/a/img/@src')
            yield Article(url, title, date, official_url, official_name, digest, image_url)


def _parse_official_node(html_text, official_node):
    """
    解析微信公众号搜索页面节点信息
    :param html_text: [str] 微信公众号搜索页面
    :param official_node: [lxml.element] 搜索页面公众号对应节点
    :return: Official对象
    """
    official_node_id = str(official_node.xpath('./@d')[0])
    monthly_data_url = 'https://weixin.sogou.com' + search('var account_anti_url = \"(.*?)\";', html_text)[1]
    monthly_data = loads(_get_html(monthly_data_url, False))['msg']
    status = monthly_data[official_node_id].split(',') if official_node_id in monthly_data else []
    status = (f'月发文: {status[0]}篇', f'月访问: {status[1]}次') if status else ()
    official_id = _extract(official_node, './div/div[2]/p[2]/label/text()')
    url = _parse_link(_extract(official_node, './div/div[2]/p[1]/a/@href'))
    name = _extract(official_node, './div/div[2]/p[1]/a', True)
    avatar_url = _extract(official_node, './div/div[1]/a/img/@src')
    qr_code_url = _extract(official_node, './div/div[3]/span/img[1]/@src')
    profile_desc = _extract(official_node, './dl[1]/dd', True)
    recent_article = None
    # 获取公众号文章
    dl_nodes = official_node.xpath('./dl[position()>1]')
    for node in dl_nodes:
        dt = _extract(node, './dt/text()')
        if dt and '最近文章' in dt:
            article_date = _extract(node, './dd/span', True)
            article_date = int(search('document.write\(timeConvert\(\'(.*?)\'\)\)', article_date)[1])
            article_date = strftime('%Y-%m-%d', localtime(article_date))
            recent_article = Article(
                url=_parse_link(_extract(node, './dd/a/@href')),
                title=_extract(node, './dd/a', True),
                date=article_date,
                official_url=url,
                official_name=name,
            )
    return Official(url, official_id, name, avatar_url, qr_code_url, profile_desc, status, recent_article)


def _get_html(url, is_proxy=True):
    """
    获取页面
    :param url: 链接
    :param is_proxy: 是否启用代理
    :return: html文本/None
    """
    if 'suv' not in _session.cookies:
        _session.get('https://pb.sogou.com/pv.gif')
    if is_proxy and setting.get_proxy:
        for _ in range(setting.repeat_times):
            proxies = setting.get_proxy()
            try: resp = _session.get(url, proxies=proxies, timeout=setting.proxy_timeout)
            except (Timeout, ProxyError, TooManyRedirects): continue
            if url == resp.url: return str(resp.content, 'utf-8')
        else:
            resp = _session.get(url)
            if url == resp.url: return str(resp.content, 'utf-8')
            setting.proxy_error_callback(url)
            return None
    else:
        resp = _session.get(url)
        if url == resp.url: return str(resp.content, 'utf-8')
        else: return _get_html(url, False) if _identify_captcha() else None


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


def _parse_link(link):
    """
    解析链接
    :param link: 链接
    """
    if not link or'&k' in link: return link
    else:
        b = randint(1, 100)
        a = link.find('url=')
        c = link[a + b + 30]
        url = f'https://weixin.sogou.com{link}&k={b}&h={c}'
        resp = _session.get(url)
        resp.encoding = 'utf-8'
        url_fragments = findall('url \+= \'(.*?)\';', resp.text)
        return ''.join(url_fragments).replace('@', '')


def _identify_captcha():
    """
    验证码识别
    :return: True/False
    """
    for _ in range(setting.repeat_times):
        _session.headers.update({'Referer': 'https://weixin.sogou.com'})
        resp = _session.get(f'http://weixin.sogou.com/antispider/util/seccode.php?tc={int(time())}')
        tf = TemporaryFile()
        tf.write(resp.content)
        code = setting.sougo_captcha_callback(Image.open(tf))
        if not code: continue
        resp = _session.post('https://weixin.sogou.com/antispider/thank.php', data={
            'c': code,
            'r': 'https://weixin.sogou.com/',
            'v': 5,
        })
        resp.encoding = 'utf-8'
        msg = resp.json()
        if msg['code'] == 0:
            add_dict_to_cookiejar(_session.cookies, {'SNUID': msg['id']})
            return True
        print('验证码错误!')
    return False
