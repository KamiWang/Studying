

default_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                   "Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}


def get_coding(response):
    charset = "utf-8"
    try:
        charset = response.get_encoding()
    except Exception:
        return charset
    if charset.find("gb") >= 0:
        charset = "gb18030"
    return charset
