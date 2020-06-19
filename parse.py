import requests
from retrying import retry

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "Referer":"https://m.douban.com/movie/nowintheater?loc_id=108288"
    }


@retry(stop_max_attempt_number=3)
def _parse_str(url):
    print("-"*10)
    response = requests.get(url,headers = headers,timeout = 5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_str(url)
    except:
        html_str = None
    return html_str

if __name__=="__main__":
    url = "https://www.baidu.com"
    print("dadadad")
    print(parse_url(url))
    print("123")
