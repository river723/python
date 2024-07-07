from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree
from urllib import parse
from multiprocessing import Process,Queue

# https://www.igdcc.com/shouji/fengjing/

def getPicUrl(q):
    url = 'https://3d.qingmo.com/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    picUrl_list = tree.xpath('//div[@class="list_img_item"]//a/@url')
    for i in picUrl_list:
        href=parse.urljoin(url,i)
        print(href)
        child_response = requests.get(href)
        child_response.encoding = 'utf-8'
        child_tree = etree.HTML(child_response.text)
        src=child_tree.xpath('//a[@class="show_l_wrap__a fullsizable-a is-active"]/@href')[0]
        q.put(src)
    q.put("over")
def download(url):
    print("开始下载"+url)
    response = requests.get(url)
    name = url.split('/')[-1]
    with open('./img/'+name,mode='wb') as f:
        f.write(response.content)

    print(name+"下载完成")
def dowload_img(q):
    with ThreadPoolExecutor(10) as t:
        while True:
            url = q.get()
            print(url+"从队列取出\n")
            if url == "over":
                break
            t.submit(download, url)


if __name__ == '__main__':
    q=Queue()
    p1=Process(target=getPicUrl,args=(q,))
    p2=Process(target=dowload_img,args=(q,))
    p1.start()
    p2.start()

# https://img.qingmo.com/21080/2024/06/03/bccf02a221a811efb253005056a64936.jpg
# https://img.qingmo.com/11080/2024/06/03/bccf02a221a811efb253005056a64936.jpg