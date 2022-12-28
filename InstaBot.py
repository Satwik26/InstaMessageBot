from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
browser=webdriver.Chrome("D:\chromedriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(1)
username=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys("your username")
time.sleep(1)
password=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys("your password")
password.submit()
time.sleep(5)
notnow=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
notnow.click()
time.sleep(1)
notif=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
notif.click()
time.sleep(1)
message=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a").click()
time.sleep(1)
sendMessage=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div").click()
time.sleep(1)
to=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input")
to.send_keys("recipient username")
time.sleep(1)
circ=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button").click()
time.sleep(1)
nxt=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button").click()
time.sleep(10)
txt_area=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("your message")
send=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
time.sleep(5)




