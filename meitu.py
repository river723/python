from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree
from urllib import parse
from multiprocessing import Process,Queue

# https://www.igdcc.com/shouji/fengjing/

def getPicUrl(q):
    url = 'https://www.igdcc.com/shouji/fengjing/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    picUrl_list = tree.xpath('//div[@class="mt15 clearfix pic-auto pic-list"]/a/@href')
    for i in picUrl_list:
        href=parse.urljoin(url,i)
        child_response = requests.get(href)
        child_response.encoding = 'utf-8'
        child_tree = etree.HTML(child_response.text)
        src=child_tree.xpath('//div[@class="preview-pic"]//a/img/@src')
        q.put(src)
    q.put("over")
def download(url):
    print("开始下载"+url)
    response = requests.get(url)
    name = url.split('/')[-1]
    with open('./img/'+name,mode='wb') as f:
        f.write(response.content)
    print("下载完成")
def dowload_img(q):
    with ThreadPoolExecutor(10) as executor:
        while True:
            url = q.get()
            if url == "over":
                break
            executor.submit(download, url)


if __name__ == '__main__':
    q=Queue()
    p1=Process(target=getPicUrl,args=(q,))
    p2=Process(target=dowload_img,args=(q,))
    p1.start()
    p2.start()

