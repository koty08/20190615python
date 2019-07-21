from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver= webdriver.Chrome('selenium/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(5)

id= 'koty08'
pw= 'kty123'

# 보안상이유로 막아놓음 
# driver.find_element_by_name('id').send_keys(id)
# driver.find_element_by_name('pw').send_keys(pw)

# 이걸 사용
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(2)

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
point = soup.select_one('.my_npoint strong')
print(point.string)
time.sleep(15)
driver.close()