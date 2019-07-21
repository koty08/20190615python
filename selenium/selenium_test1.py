from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Chrome('selenium/data/chromedriver')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
time.sleep(10)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(10)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[5].click()
time.sleep(10)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li2 = gugun.find_elements_by_tag_name('li')
li2[-1].click()
time.sleep(10)

source = driver.page_source

bs = BeautifulSoup(source, 'lxml')
entire = bs.find('ul', class_ = 'quickSearchResultBoxSidoGugun')
li_list = entire.find_all('li')

for li in li_list:
    print(li.find('p').text)