import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def base64_api( b64,uname='river723', pwd='5X9a51405', typeid=27):

    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""

web=webdriver.Edge()
web.get("https://login.51job.com/")
web.implicitly_wait(10)
web.find_element(By.XPATH,'//*[@id="NormalLoginBtn"]/span[3]/a').click()
web.find_element(By.XPATH,'//*[@id="loginname"]').send_keys("135351594")
web.find_element(By.XPATH,'//*[@id="password"]').send_keys("123456")
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="signup"]/div[4]/label').click()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="login_btn_withPwd"]').click()
time.sleep(2)
verify_div=web.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[6]')
# /html/body/div[5]/div[2]/div[6]
# verify_div.screenshot('tu.png')
tu=verify_div.screenshot_as_base64
verify_code=base64_api(tu)
print(verify_code)
for p in verify_code.split('|'):
    x=p.split(',')[0]
    y=p.split(',')[1]
    print(x,y)
    ActionChains(web).move_to_element_with_offset(verify_div,int(x),int(y)).click().perform()
    time.sleep(2)
time.sleep(20)
web.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[6]/div/div/div[3]/a').click()
time.sleep(20)


