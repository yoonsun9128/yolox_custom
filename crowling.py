from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import os


driver = webdriver.Chrome('/Users/triplet/Downloads/chromedriver_mac64') # 크롬드라이버 설치한 경로 작성 필요 
url = "https://auto.danawa.com/auto/?Work=home"
driver.get(url)

urls = driver.find_elements(By.CLASS_NAME,'branditem')
url_list = []

img_folder = './img'

file_list = os.listdir(img_folder)
file_count = len(file_list)
print(file_count)

for url in urls:
    time.sleep(1)
    path = url.find_element(By.TAG_NAME, 'a').get_attribute('href')
    # print(path)
    # url_list.append(path)
    driver.get(path)
    plants = driver.find_elements(By.TAG_NAME, "img")
    for plant in plants:
        car = plant.get_attribute('src')
        if "model" in car:
            if file_count< 100:
                cv2.imwrite(img_folder, car)
                print(car)
            else:
                driver.close()


# for i in url_list:
#     driver.get(i)
#     time.sleep(1)
#     plants = driver.find_elements(By.TAG_NAME, "img")
#     for plant in plants:
#         car = plant.get_attribute('src')
#         if "model" in car:
#             if file_list< 100:
#                 os.imwrite(img_folder, car)
#                 print(car)
#             else:
#                 driver.close()

        


