import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import csv
from pyquery import PyQuery as pq

if __name__ == '__main__':
    url = 'http://www.haozhanhui.com/place/1595.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }
    req = requests.get(url, headers=headers)
    req.encoding = req.apparent_encoding
    html = requests.get(url).content
    html = html.decode()
    # print(html)
    # doc = pq(html)
    #
    '''通过panad读取html文件,得到table'''

    # soup = BeautifulSoup(html, 'lxml')
    # content = soup.select('.tbsty')[0]
    # content_obj=StringIO(content.prettify())
    # print(type(content))
    # df=pd.read_html(content_obj)[0]
    # # df = pd.DataFrame(data_list)
    # print(df)
    # df.to_csv('Jinyang_Lake.csv', index=False)

    '''通过pyquery读取html文件,得到内容'''
    doc = pq(html)
    exhi_list = []
    # content = doc('.tbsty tbody tr:nth-child(2n) td')
    for row in doc('table.tbsty tr').items():

        name=row.find("td").eq(1).text()
        date=row.find("td").eq(2).text()
        title=row.find("td").eq(3).text()

        # print(name,date,title)
        if name != "":
            exhi_list.append(
                {
                    '名称': name,
                    '时间': date,
                    '主题': title
                }
            )


    exhi_list.remove(exhi_list[0])

    print(exhi_list)

