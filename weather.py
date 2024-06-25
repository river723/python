import requests
from lxml import etree
import csv

url = "http://www.weather.com.cn/weather1d/101100101.shtml"
headers={
    "User-Agent" :"User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding="utf-8"
et=etree.HTML(response.text)
divs=et.xpath('//*[@id="around"]/div[@class="aro_city"]/ul/li[2]/a/span/text()')

print(divs)
