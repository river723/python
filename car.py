import requests
from pyquery import PyQuery


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    print(response.text)


def parse_page(html):
    pass


def main():
    url = 'https://k.autohome.com.cn/6962'
    html = get_page(url)
    parse_page(html)


if __name__ == '__main__':
    main()
