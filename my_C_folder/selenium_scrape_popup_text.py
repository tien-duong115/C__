from re import search
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

PATH = "chromedriver.exe"
m = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(7) > ul > li:nth-child(1) > span > a'
driver = webdriver.Chrome(PATH)
driver.get('https://catalog.sjsu.edu/preview_program.php?catoid=12&poid=3979&returnto=4146')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, m))).click()
time.sleep(5)
ele = driver.find_element_by_xpath(n)
html = ele.get_attribute('outerHTML')
attrs = BeautifulSoup(html, 'html.parser')
print(attrs.text) 

# like = driver.find_elements_by_class_name('acalog-course')
# for x in range(0,len(like)):
#     time.sleep(1)
#     if like[x].is_displayed():
#         time.sleep(1)
#         like[x].click()