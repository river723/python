import requests
import execjs
import json
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'text/xml;charset=UTF-8',
    'Origin': 'https://ccprec.com',
    'Referer': 'https://ccprec.com/navCqzr/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# data = '0047n982r3f1l1unl1tp4l8ucg9i4g5e457a4g65497k6b707r7566885k4c7s4u725n7h5e5r5n5y4t6s7s887r7x446k6x7c5u7w614w9768958t6n4y70414d5p6n4v5t686t446u9j876o9d837l86507w8k59656a434t5v7v567m5z5x4z627d906o8u7b7i8f5o8g97856l8r6i7p6g7p62813r7k4q5r6b7h5o6z7w625x56626x8s6r85657s697c6z784v735l6t7u6k3r6j7f3u7h4g7w7u8y7n716c7o696w5x747g89547g7n6t477a7i4v6m5z6g7m6o3z655f657k7n5p7r5h7k5y7l776a577p7s7d89575s787i3z6i6c6c6m9a6e9a6j695w8m7f9g4r7e8778745r8f6j65575y41605h6m4g7q5d5e518h646m5y83996m7k4f765z6z4h5s525o5y7q5r745369496j706n567n8w595u5m7n666h6e646g5d3s6e597d7o7i5t6i7l9g747z964o894c7z8f7y515w6g5d456r605w52824k816e776g8o7h6r7769806v7f66795q4u585m4b7m4n6t497k8l746o9r7y6f7h6h9q7q5i668f487y5p7d4l8o7g8n7h92866j5p7p8v6s6q5t9e8u716i8x6o6v7n8g7p855d7l6y809b5j4b6y785x746371646y415q5w6i6z7j7m6n47725r6o6o7t4k836w46625e5y727f6b7s7o5o5l8d57695h5g49826c6y4r797a47'
data = '005zumfelwo1dcifq945steydm18xdf15xm5w6o5k746c6e497c7p6o7j7a6e6g3x638063765o7n564e7e76694z7u8q9f7y7j5z8r7g944b5l7h8s8w8x83584u7a5o5m7o696h4c6f755j6f7u6o8n96808z7z6g7y8w3r7c645f637m6a57697t656f6673916o767j8u895h6o9s8b818o7q958d7m607z557h675n4u5x5s6y807f6a6e5u5j7h8i807e7l6c7i8l7f6c6w786v7v4x566278587m4h636k9a9a8v808h696g5t7q7a7x6u619o6u5v6w776f6x7i4k7n6k5b626z667m5y7h856x7x7d7d5i4u76797i7a6q6z5k7i7h576l827v6l8w7q9d806e646t5u9n6m6z8g8k755k6q74626g4e3x7s746h5v7p705p6r6l5u6d7i7p9a6r604c746g6x695n6i5h647w7474534q686b6z6h6m7f936w476u756c6g7y4s6b5a5l6g6n7w937j5t6r7r938e7q708f6r7e76908d6r62686l5i6i7f675a6i4o7z6k708g887e6o5r817j6y5x627o766b6o595w836d565o728g6y8g846a6g7o859a8c5f7m6v479q73714j7b9f8o958n7x6j7n7k74846h768z985r6d7h8a8j928n928c5d658x7j933w4f72757i6y7c6s6o763t5l727v8f7i7s594b797m686z7l68685c635u6o425s7w7r7w8x6x778i6v4s6w575t7n6f5j4u5i7d5z'
with open('ccprec.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)
result=ctx.call('main123', 1)
print(result)

response = requests.post('https://ccprec.com/honsanCloudAct', headers=headers, data=result)
response.encoding = 'utf-8'
print('--------------')
print(response.text)
print('--------------')
resultData=ctx.call('decryptCode', response.text)
# for i in json.loads(resultData):
#     print(i)
print(resultData)