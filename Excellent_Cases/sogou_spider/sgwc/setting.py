from requests import Session


def _sougo_captcha_callback(captcha_image):
    """Sougo识别验证码回调函数"""
    captcha_image.show()
    return input('请输入Sougo验证码: ')


def _wechat_captcha_callback(captcha_image):
    """Wechat识别验证码回调函数"""
    captcha_image.show()
    return input('请输入WeChat验证码: ')


def _wechat_link_error_callback(url):
    """Wechat链接失效回调函数"""
    print(f'Link error: {url}.')


def _proxy_error_callback(url):
    """代理失败回调函数"""
    print(f'Proxy error: {url}.')


def _get_session():
    session = Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36 ',
    }
    return session


get_session = _get_session  # 设置获取session对象函数
sougo_captcha_callback = _sougo_captcha_callback
wechat_captcha_callback = _wechat_captcha_callback
wechat_link_error_callback = _wechat_link_error_callback
repeat_times = 3  # 验证码/代理失败重复次数
get_proxy = None  # 设置获取代理函数, 返回 {'http': 'http://127.0.0.1:80', 'https': 'http://127.0.0.1:80'}
proxy_timeout = 10  # 代理超时设置
proxy_error_callback = _proxy_error_callback
