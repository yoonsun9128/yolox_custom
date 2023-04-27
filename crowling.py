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
url = "https://www.google.co.kr/search?q=car&hl=ko&authuser=0&tbm=isch&source=hp&biw=1440&bih=821&ei=ojZKZJGqCsan-QbSrb2wAQ&iflsig=AOEireoAAAAAZEpEspPgoUXtfwUu2scN7yOsYF8Eggyp&ved=0ahUKEwiRg5DB1sn-AhXGU94KHdJWDxYQ4dUDCAc&uact=5&oq=car&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIICAAQgAQQsQM6BAgAEANQAFiQBGDyCGgAcAB4AIABcYgBvAKSAQMxLjKYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img"
driver.get(url)

name = 'car'
path = './img'

imgs = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")

for img in imgs:
    try:
        time.sleep(2)
        imgUrl = img.get_attribute("src")
        print(imgUrl)
        urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")
        count = count + 1
        if count > 100: #다운 받을 이미지 갯수 조정
            break
    except:
            pass
# file_list = os.listdir(img_folder)
# file_count = len(file_list)
# print(file_count)

# for url in urls:
#     time.sleep(1)
#     path = url.find_element(By.TAG_NAME, 'a').get_attribute('href')
#     # print(path)
#     # url_list.append(path)
#     driver.get(path)
#     plants = driver.find_elements(By.TAG_NAME, "img")
#     for plant in plants:
#         car = plant.get_attribute('src')
#         if "model" in car:
#             if file_count< 100:
#                 cv2.imwrite(img_folder, car)
#                 print(car)
#             else:
#                 driver.close()


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

        


