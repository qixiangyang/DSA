# Sgwc
搜狗微信文章、公众号爬虫接口。

## 安装 
```
pip3 install sgwc --upgrade
```

## 使用
```
from sgwc import get_official, search_officials, search_articles, get_hot_articles

official = get_official(official_id='official_id')  # 通过微信号获取指定公众号
officials = search_officials(keyword='keyword')  # 通过关键字搜索公众号
articles = search_articles(keyword='keyword')  # 通过关键字搜索文章
articles = get_hot_articles()  # 获取热门文章
```
#### 从 Article、Official 实例对象提取相关信息
```
article.url
article['url']  # 可以像字典类型一样, 提取信息(但不是字典类型)
article.items()  # 返回可遍历的(键, 值) 元组数组
```
#### setting
```
from sgwc import setting

# 自定义设置获取session对象函数, 返回: Session对象
# 详见: https://2.python-requests.org//en/master/user/advanced/#session-objects
setting.get_session = get_session

# 自定义搜狗验证码回调函数, 参数: 验证码图片(pillow Image 对象), 返回: 验证码
setting.sougo_captcha_callback = sougo_captcha_callback

# 自定义微信验证码回调函数, 参数: 验证码图片(pillow Image 对象), 返回: 验证码
setting.wechat_captcha_callback = wechat_captcha_callback

# 微信链接异常回调函数(系统出错/链接过期), 参数: 链接
self.wechat_link_error_callback = _wechat_link_error_callback

# 验证码/代理错误(代理不可用或超时)重复次数, 超过重复次数将跳过
setting.repeat_times = 3

# 自定义获取代理函数
# 返回格式: {'http': 'http://127.0.0.1:80', 'https': 'http://127.0.0.1:80'}
# 详见: https://2.python-requests.org//en/master/user/advanced/#proxies
setting.get_proxy = get_proxy 

setting.proxy_timeout = 10  # 代理超时设置

# 代理使用失败回调函数(当代理失败达到重复次数将会调用), 参数: 链接
setting.proxy_error_callback = proxy_error_callback
```
- 当设置了 `get_proxy` 函数，将不会执行验证码回调函数

## API
#### get_official(official_id)
- official_id: 微信号
- 返回 `Official` 对象或 `None`

#### search_officials(keyword, pages=1, begin_page=1)
- keyword: 搜索关键字
- pages: 获取页面数量
- begin_page: 起始页
- 返回 `Official-Generator` 对象

#### search_articles(keyword, pages=1, begin_page=1)
- keyword: 搜索关键字
- pages: 获取页面数量
- begin_page: 起始页
- 返回 `Article-Generator` 对象

#### get_hot_articles(pages=2, article_type=0)
- pages: 获取页面数量
- article_type: 文章类型
- 返回 `Article-Generator` 对象

###### article_type 对照表
| 数值 | 类型 |
|:----:|:----:|
| 0 | 热门 |
| 1 | 搞笑 |
| 2 | 养生堂 |
| 3 | 私房话 |
| 4 | 八卦精 |
| 5 | 科技咖 |
| 6 | 财经迷 |
| 7 | 汽车控 |
| 8 | 生活家 |
| 9 | 时尚圈 |
| 10 | 育儿 |
| 11 | 旅游 |
| 12 | 职场 |
| 13 | 美食 |
| 14 | 历史 |
| 15 | 教育 |
| 16 | 星座 |
| 17 | 体育 |
| 18 | 军事 |
| 19 | 游戏 |
| 20 | 萌宠 |


#### Article
| 属性 | 返回类型 | 说明 |
|------|:--------:|------|
| url | str | 链接 |
| title | str | 标题 |
| date | str | 发布日期 |
| image_url | str | 图片链接 |
| digest | str | 文章概述 |
| official_url | str | 公众号链接 |
| official_name | str | 公众号名称 |
| save_article(save_path='.') | None | 保存文章为 Markdown 文件(save_path: 保存路径) |
| items() | list | 返回可遍历的(键, 值) 元组数组 |
| get_html() | str | 返回文章html |

#### Official
| 属性 | 返回类型 | 说明 |
|------|:--------:|------|
| url | str | 链接 |
| official_id | str | 微信号 |
| name | str | 公众号名称 |
| avatar_url | str | 公众号头像链接 |
| qr_code_url | str | 公众号二维码链接 |
| profile_desc | str | 公众号简介 |
| status | tuple | 公众号每月状态, (每月发文数, 每月访问数) |
| recent_article | Article | 最新文章 Article 实例 |
| articles | \[Article\] | 公众号文章 Article 实例数组 |
| authenticate | str | 认证 |
| from_url(url) | Official | 类方法, 通过公众号链接生成 Official 实例 |
| items() | list | 返回可遍历的(键, 值) 元组数组 |
