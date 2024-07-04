import requests
from pyquery import PyQuery as pq
import pymysql

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
    html=get_page(url)

    doc = pq(html)
    title = doc('body > div.main.w1000 > div.heading1.w1000.mt20.clearfix > h1').text()
    summary = doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.summary > p').text()
    contentTemp = doc('body  div.main.w1000  div.article.clearfix  div.main_left.fl  div.article_con')
    # contentTemp = doc('.article_con')
    contentTemp.remove('script')
    content=contentTemp.outer_html()
    nextPageUrl=doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.listPage > a:contains("下一页")').attr('href')
    while nextPageUrl:

        tempDoc = pq(url=nextPageUrl,encoding='utf-8')
        contentTemp = tempDoc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.article_con')
        contentTemp.remove('script')
        content+=contentTemp.outer_html()
        nextPageUrl=tempDoc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.listPage > a:contains("下一页")').attr('href')
    strSql="insert into stocknews(title,summary,content) values('{}','{}','{}')".format(title,summary,content)
    cursor.execute(strSql)
    db.commit()
    print(content)
def main():


    url = 'https://stock.cngold.org/rumen'
    html = get_page(url)
    url_list = get_urls(html)
    for url in url_list:
        print(url)
        parse_page(url)
    # parse_page('https://stock.cngold.org/rumen/c6694940.html')
    db.close()

if __name__ == '__main__':
    db=pymysql.connect(host='localhost',user='root',password='123456',db='pydata', charset='utf8mb4')
    cursor=db.cursor()
    main()