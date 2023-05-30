# from selenium import webdriver
# import os
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
#
# options = Options()
#
#
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
#
# class bot:
#     def __init__(self,username):
#
#         self.username=username
#
#         self.base_url='https://chat.openai.com/chat'
#         self.bot=driver
#         self.login()
#
#     def login(self):
#
#
#         self.bot.get(self.base_url)
#         time.sleep(30)
#         enter_username=WebDriverWait(self.bot,20).until(expected_conditions.presence_of_element_located((By.TAG_NAME,'textarea')))
#         enter_username.send_keys(self.username)
#
#         enter_username.send_keys(Keys.RETURN)
#           #This is for Press Enter
#         print( driver.title)
#         time.sleep(10)
#         #print( driver.find_element(By.CLASS_NAME,'x1i10hfl').text)
#
# def init():
#     b1=bot('Hello how are you')
#
#
#
# init()

#_________________________________________________________________________________
import requests
import time
from bs4 import BeautifulSoup
api='https://chat.openai.com/chat'
r=requests.get(api)
data=BeautifulSoup(r.text,"html.parser")
time.sleep(20)
# temp=data.find("div",tag_="textarea").text
# print(temp)