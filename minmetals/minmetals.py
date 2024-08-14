import requests
import execjs
cookies = {
    '__jsluid_s': '18a71bbf644a16456d156d8a3f15859d',
    'SUNWAY-ESCM-COOKIE': 'a8037be9-8a62-4ec3-b61b-fdea17cc237f',
    'JSESSIONID': '839C2A9154B9B7431929DCDAB70334E9',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': '__jsluid_s=18a71bbf644a16456d156d8a3f15859d; SUNWAY-ESCM-COOKIE=a8037be9-8a62-4ec3-b61b-fdea17cc237f; JSESSIONID=839C2A9154B9B7431929DCDAB70334E9',
    'Origin': 'https://ec.minmetals.com.cn',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response1 = requests.post('https://ec.minmetals.com.cn/open/homepage/public', cookies=cookies, headers=headers).text
print(response1)
print('-------')
with open('minmetals.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)

result=ctx.call('main123', response1, 1)

print(result)

json_data = {
    'param': result
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
    cookies=cookies,
    headers=headers,
    json=json_data,
).text
print(response)
