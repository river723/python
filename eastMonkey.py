import requests
import re
import execjs
import json
cookies = {
    'qgqp_b_id': 'bea1524725e39936123e5b6d7cd5155e',
    'websitepoptg_api_time': '1721718049290',
    'st_si': '51053668519085',
    'st_asi': 'delete',
    'st_pvi': '15944523006363',
    'st_sp': '2024-07-23%2015%3A00%3A49',
    'st_inirUrl': 'https%3A%2F%2Fwww.bing.com%2F',
    'st_sn': '5',
    'st_psi': '20240723150213459-117001314791-6039009578',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'qgqp_b_id=bea1524725e39936123e5b6d7cd5155e; websitepoptg_api_time=1721718049290; st_si=51053668519085; st_asi=delete; st_pvi=15944523006363; st_sp=2024-07-23%2015%3A00%3A49; st_inirUrl=https%3A%2F%2Fwww.bing.com%2F; st_sn=5; st_psi=20240723150213459-117001314791-6039009578',
    'Referer': 'https://guba.eastmoney.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


params = {
    'type': '0',
    'sort': '0',
    'page': '2',
    'v': '2024_7_24_11_0',
}

response = requests.get('https://gbcdn.dfcfw.com/rank/popularityList.js', params=params, headers=headers)
data=re.findall(r"var popularityList='(.*)'", response.text)[0]
# print(data)

jscode=open('eastMonkey_jscode.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(jscode)
scriptdata=ctx.call('main123', data)
# print(scriptdata)
t_list = []
for i in scriptdata:
    t_list.append(i['code'])
t_str = ','.join(t_list)
print(t_str)
print('------------------')
secId=ctx.call('getHQSecIdByMutiCode',t_str)
# print(secId)

# https://guba.eastmoney.com/rank/
jsonp_response = requests.get(
    'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&np=3&ut=a79f54e3d4c8d44e494efb8f748db291&invt=2&secids='+secId+'&fields=f1,f2,f3,f4,f12,f13,f14,f152,f15,f16&cb=qa_wap_jsonpCB1721718133048',
    cookies=cookies,
    headers=headers,
).text
start = jsonp_response.find('(') + 1
end = jsonp_response.rfind(')')
json_data = jsonp_response[start:end]
data = json.loads(json_data)
data_list = data['data']['diff']
for i in data_list:
    print(i)