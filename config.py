from nonebot.default_config import *

HOST = '0.0.0.0'
PORT = 8080

NICKNAME = {'ELF', 'elf'}

COMMAND_START = {'', '/', '!', '／', '！'}

SUPERUSERS = {123456789} # 管理员（你）的QQ号

API_ROOT = 'http://127.0.0.1:5700'     #
RSS_PROXY = '127.0.0.1:7890'    # 代理地址
ROOTUSER=[123456]    # 管理员qq,支持多管理员，逗号分隔 如 [1,2,3] 注意，启动消息只发送给第一个管理员
DEBUG = False
RSSHUB='https://rsshub.app'     # rsshub订阅地址
DELCACHE=3     #缓存删除间隔 天
LIMT=50 # 缓存rss条数

# 解决pixiv.cat无法访问问题
CLOSE_PIXIV_CAT=True #是否关闭使用 pixiv.cat，关闭后必须启用代理
# 以下两项在关闭使用 pixiv.cat时有效，如果你有自己反代pixiv，填上你自己的反代服务器地址即可，没有不要填
PIXIV_REFERER='http://www.pixiv.net' # 请求头 referer 设置
PIXIV_PROXY='i.pximg.net' # 反代图片服务器地址
# 此处推荐一个反代网站 http://pixivic.com   original.img.cheerfun.dev


# MYELF博客地址 https://myelf.club
# 出现问题请在 GitHub 上提 issues
# 项目地址 https://github.com/Quan666/ELF_RSS
# v1.2.4