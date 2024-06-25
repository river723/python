import requests
import re
headers={
    "User-Agent" :"User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    'Cookie' :'__mta=152006918.1718847107095.1719277182224.1719277318632.23; uuid_n_v=v1; uuid=DBFED5402EA411EF821D05E7E9987C0C6D6079FE195241AB9A591C5EB9359BC5; _lxsdk_cuid=19033456c50c8-0146b9ee0d9fc9-4c657b58-240000-19033456c51c8; _lxsdk=DBFED5402EA411EF821D05E7E9987C0C6D6079FE195241AB9A591C5EB9359BC5; __mta=152006918.1718847107095.1718847107095.1718847107095.1; _csrf=064981f33e8540693e3d78eafdcf4e70cf7055298e3a617c0038e68e868245a6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1718847106,1719276384; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1719277318; _lxsdk_s=1904cdbaf84-ef3-34e-383%7C%7C20'
}


def parse_html(html):
    pattern=re.compile('<p class="name"><a href=".*?" title="(.*?)" data-act="boarditem-click" data-val="{movieId:\\d+}">(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            '名称': item[1],
            '主演': item[2].strip(),
            '时间': item[3]
        }
        # print(item)

def save_data():
    f=open('maoyan_top100.txt','w',encoding='utf-8')
    for i in range(5):
        url='https://www.maoyan.com/board/4?offset='+str(i*10)
        print(url)
        response=requests.get(url,headers=headers)
        # print(html)
        for item in parse_html(response.text):
            f.write(str(item)+'\n')
    f.close()



if __name__ == '__main__':
    save_data()