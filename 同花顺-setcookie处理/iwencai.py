import requests
import execjs

with open('getcookie.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)
v=ctx.call('main123')

cookies = {
    'ta_random_userid': 'kkg2mk6ojl',
    'v': v,
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'ta_random_userid=kkg2mk6ojl; v=A12vZmbG52jC8YNs109gUyCmbDJSepoYm671wx8mmbTj1nOs58qhnCv-BVus',
    'Origin': 'https://www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.iwencai.com/unifiedwap/result?w=5g&querytype=stock&addSign=1723619485078',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'hexin-v': 'A12vZmbG52jC8YNs109gUyCmbDJSepoYm671wx8mmbTj1nOs58qhnCv-BVus',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'source': 'Ths_iwencai_Xuangu',
    'version': '2.0',
    'query_area': '',
    'block_list': '',
    'add_info': '{"urp":{"scene":1,"company":1,"business":1},"contentType":"json","searchInfo":true}',
    'question': '5g',
    'perpage': 50,
    'page': 1,
    'secondary_intent': 'stock',
    'log_info': '{"input_type":"typewrite"}',
    'rsh': None,
}

response = requests.post(
    'https://www.iwencai.com/customized/chart/get-robot-data',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()

print(response)

