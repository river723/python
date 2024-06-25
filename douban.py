import requests
from bs4 import BeautifulSoup
import csv
headers={
    "User-Agent" :"User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

# for start_num in range(0,250,25):
#     response = requests.get(f'https://movie.douban.com/top250?start={start_num}', headers=headers)
#     html=response.text
#     soup=BeautifulSoup(html,'html.parser')
#     all_title=soup.find_all('span',class_='title')
#     for title in all_title:
#         title_string=title.get_text()
#         if "/" not in title_string:
#             print(title_string)

response = requests.get('https://movie.douban.com/top250', headers=headers)
html=response.text
soup=BeautifulSoup(html,'lxml')
movie_list=soup.find('ol',class_='grid_view').find_all('li')
# print(movie_list)
f=open('douban.csv','a',newline='',encoding='utf-8')
writer=csv.writer(f)
writer.writerow(['电影名','评分','评论'])
for movie in movie_list:
    # title=movie.find('div',class_='hd').find('span',class_='title').get_text()
    title=movie.find('span',class_='title').get_text()
    rating_num=movie.find('span',class_='rating_num').get_text()
    comment_num=movie.find('div',class_='star').find_all('span')[3].get_text()
    writer.writerow([title,rating_num,comment_num])
    # print(title,rating_num,comment_num)
f.close()