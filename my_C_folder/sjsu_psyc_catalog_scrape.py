from re import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import requests
from bs4 import BeautifulSoup as bs

PATH = "chromedriver.exe"
url = 'https://catalog.sjsu.edu/content.php?catoid=12&catoid=12&navoid=4145&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=46'
catalog_url = "https://catalog.sjsu.edu/content.php?catoid=12&catoid=12&navoid=4145&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=46"
data = requests.get(catalog_url)
course_href = []
my_link = []
for i in bs(data.text,"html.parser").find_all('a', href=True):
    if search('preview_course' ,i['href']):
        course_href.append(i['href'])
for link in course_href:
    my_link.append(f"//a[contains(@href,'{link}')]")

driver = webdriver.Chrome(PATH)
driver.get(url)
my_count = 0
for link in my_link:
    driver.find_element_by_xpath(link).click()
    time.sleep(0.15)
    my_count+=1
time.sleep(2)
# new_data = bs(driver.find_element_by_xpath("//table[@class='td_dark']").get_attribute('outerHTML'), 'html.parser')
my_list_of_string = []
try:
    for content in range(3,my_count+1):
        my_list_of_string.append(bs(driver.find_element_by_xpath(f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{content}]/td[2]/table/tbody/tr/td/div[2]').get_attribute('outerHTML'), 'html.parser').text)
except NoSuchElementException:
    pass

with open('course_description.txt','w') as file:
    for line in my_list_of_string:
        file.write("%s\n" % line)
     
count = 0
my_list = []
with open('course_description.txt') as f:
    for line in f:
        my_list.append(f.readline())
        
keys = [ e[:e.index('-')].replace(' ','') for e in my_list]
values = [ e[e.index('- '):].replace('- ','') for e in my_list]