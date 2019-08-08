import time
from selenium import webdriver
from bs4 import BeautifulSoup

open_driver = webdriver.Chrome()
# open_driver = webdriver.Firefox()
# open_driver = webdriver.PhantomJS()
open_driver.get("https://www.mgtv.com/b/100964/1015328.html")
time.sleep(5)
content = open_driver.page_source.encode('utf-8')
soup = BeautifulSoup(content, 'html.parser')
play_count = soup.find("span", {"class": "v-panel-count v-panel-mod"}).text
duration = soup.find("mango-progresstime-total-value").text
print(duration)
open_driver.close()
