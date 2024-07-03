import requests
from pyquery import PyQuery as pq

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
           }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text
def  get_urls(html):
    doc = pq(html)
    items = doc('.news_list li a').items()
    print(items)
    for item in items:
        # title = item.text()
        url=item.attr('href')
        # print(title,url)
        # yield{
        #     'title': title,
        #     'url': url
        # }

        yield url
def parse_page(url):

    doc = pq(url=url,encoding='utf-8')
    title = doc('body > div.main.w1000 > div.heading1.w1000.mt20.clearfix > h1').text()
    summary = doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.summary > p').text()
    print(title,summary)
def main():
    url = 'https://stock.cngold.org/rumen'
    html = get_page(url)
    url_list = get_urls(html)
    for url in url_list:
        print(url)
        parse_page(url)

if __name__ == '__main__':
    main()