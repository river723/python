import requests
import asyncio
from lxml import etree
from urllib import parse
import aiohttp

def parser_join(url,list):
    for i in list:
        i=url+i
        yield i
def get_everyone_url(url):
    req=requests.get(url)
    req.encoding='gbk'
    html=req.text
    tree=etree.HTML(html)
    url_list=tree.xpath('//ul[@id="section-list"]/li/a/@href')
    url_list_all=parser_join(url,url_list)
    return url_list_all

async def down_book(url):
    async with aiohttp.ClientSession() as session:

        async with session.get(url) as resp:

            html=await resp.text(encoding='gbk')
            tree=etree.HTML(html)
            book_name=tree.xpath('//div[@class="section-opt"]/h1/text()')[0]
            content=tree.xpath('//div[@id="content"]/text()')[0]
            async with open('./book/'+book_name+'.txt','w',encoding='utf-8') as f:
                 await f.write(content)

async def main():
    url='https://www.biquge635.com/book/53041/'
    url_list=get_everyone_url(url)
    tasks=[]
    for url in url_list:
        t=asyncio.create_task(down_book(url))
        tasks.append(t)
        break
    await asyncio.wait(tasks)



if __name__ == '__main__':
    asyncio.run(main())