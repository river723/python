import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent" :"User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

response = requests.get('https://www.shifair.com/galleryDetails/1039', headers=headers)
html=response.text
# print(html)
soup=BeautifulSoup(html,'html.parser')
exhibList=soup.find('div',class_='zg_body_right_block_item_list_con').find('ul').find_all('li')
print(exhibList)