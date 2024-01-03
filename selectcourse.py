from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

#设置微信提醒
# data = {
#         "appToken":'AT_dBC0kiaXFDbbaxKdPsnnsBVFVJRxaUtO',
#         "content":'msg:要发送的消息',
#         "topicIds":['9324',],
#         "summary":msg[:99], # 该参数可选，默认为 content 的前10个字符
#         "contentType":1,
#         "uids":['UID_4SpxxRkSyS5zfEXokp7tYaZQDuHh', ],
#         }
# webapi = 'http://wxpusher.zjiecode.com/api/send/message'

driver = webdriver.Edge()

# 访问网页
driver.get('https://one.uf.edu/myschedule/')
# 等待验证
time.sleep(20)
driver.get('https://one.uf.edu/myschedule/')
# 等待指定元素出现
while True:
    try:
        
        addbutton  = driver.find_element_by_xpath("//*[text()='+ Add Class']")
        addbutton.click()
        time.sleep(3)    
        button = driver.find_element_by_xpath("//*[text()='Add']")
        button.click()
        time.sleep(8)
        print('The element you are looking for is available now!')
        # 发送微信消息
        # result = requests.post(url=webapi,json=data)
        break
        
        
    except:
        # print('The element you are looking for is not found.')
        driver.refresh()
        time.sleep(5)
        # driver.get('https://one.uf.edu/soc/registration-search/2238?term="2238"&category="CWSP"&prog-level="GRAD"&dept="19140000"&course-title="Computer+and+Network+Security"')
        continue
# 关闭浏览器
driver.quit()
