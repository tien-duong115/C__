# !pip install selenium
# !apt-get update # to update ubuntu to correctly run apt install
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from re import search
import time,datetime
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
from collections import defaultdict
# Chrome browser and driver option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
# Static GLOBAL variables
catalog_url = "https://catalog.sjsu.edu/content.php?catoid=12&catoid=12&navoid=4145&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=46"
export_file_name = "course_description.txt"
data = bs(requests.get(catalog_url).text, "html.parser").find_all("td", class_="width")
dd = defaultdict(list)
curr_date = datetime.datetime.now()

def scraping_sjsu_catalog(catalog_url):
    data = requests.get(catalog_url)
    course_href = []
    my_link = []
    try:
        for i in bs(data.text,"html.parser").find_all('a', href=True):
            if search('preview_course' ,i['href']):
                course_href.append(i['href'])
        for link in course_href:
            my_link.append(f"//a[contains(@href,'{link}')]")
    except Exception as error:
        print(f"\n >>> FAIL at finding elemenet inside course catalog at {curr_date}")
        print(error)
    try:
        driver.get(catalog_url)
        my_count = 0
        for link in my_link:
            driver.find_element_by_xpath(link).click()
            time.sleep(0.5)
            my_count+=1
    except Exception as error:
        print(f"\n >>> FAIL at clicking element with selenium at {curr_date}")
        print(error)
    time.sleep(2)
    # Getting content within the expath and export it out as a txt file
    my_list_of_string = []
    try:
        for content in range(3,my_count):
            my_list_of_string.append(bs(driver.find_element_by_xpath(f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{content}]/td[2]/table/tbody/tr/td/div[2]').get_attribute('outerHTML'), 'html.parser').text)
    except NoSuchElementException:
        pass
    try:
        with open(export_file_name,'w') as file:
            for line in my_list_of_string:
                file.write("%s\n" % line)
    except Exception as error:
        print(f"\n >>> FAIL to export text file! {curr_date}")
        print(error)  
def get_course_name(data):
    keys,values=[], []
    for e in data:
        keys.append(e.text.split()[1]+e.text.split()[2])
        values.append(e.text.split()[4:])
    new_values = [' '.join(o) for o in values]
    dict_1 = dict(zip(keys,new_values))
    return dict_1
def get_course_description(file_dir):
    my_list = []
    with open(file_dir) as f:
        for line in f:
            my_list.append(line)
    keys = [ e[:e.index('-')].replace(' ','') for e in my_list]
    values = [ e[e.index('- '):].replace('- ','') for e in my_list]
    dict_2 = dict(zip(keys,values))
    return dict_2
# Create two dicts
dict_1 = get_course_name(data)
dict_2 = get_course_description(export_file_name)
# to dataframe
for d in (dict_1, dict_2):
    for key, value in d.items():
        dd[key].append(value)
df = pd.DataFrame.from_dict(dd,orient='index', columns=['name', 'description'])
# dataframe here
df