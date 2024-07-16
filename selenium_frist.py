# from selenium import webdriver
#
# driver = webdriver.Edge()
# driver.get("https://www.baidu.com")
# print(driver.title)

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
opt= Options()
opt.add_argument("--disable-gpu")
opt.add_argument("--headless")

web = Edge(options=opt)
web.get("https://tiepizi.com/splay/324202-1-1/")

iframe=web.find_element(By.XPATH,'//*[@id="playleft"]/iframe')
time.sleep(5)
web.switch_to.frame(iframe)
time.sleep(10)

times=web.find_element(By.XPATH,'//*[@class="dplayer-icons dplayer-icons-left"]/span/span[2]')
print(times.text)