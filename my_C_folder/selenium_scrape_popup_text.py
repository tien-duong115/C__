import re
from urllib import request
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup

PATH = "chromedriver.exe"
psyc_ba_2021_2022_url = "https://catalog.sjsu.edu/preview_program.php?catoid=10&poid=2880&returnto=741#year2"
whole_catalog_url = "https://catalog.sjsu.edu/preview_program.php?catoid=10&poid=2880&returnto=741"
course_description_data = 'course_description_data.txt'

psyc_1_intro_button = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(2) > div:nth-child(1) > ul > li:nth-child(2) > div > a'
hist_15 ='#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(2) > div:nth-child(1) > ul > li:nth-child(5) > div:nth-child(8) > a'
biol21 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(2) > div:nth-child(2) > ul > li:nth-child(2) > div:nth-child(1) > a'
stat95 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(2) > div:nth-child(2) > ul > li:nth-child(3) > div > a'
AFAM_2B ='#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(2) > div:nth-child(2) > ul > li:nth-child(5) > div:nth-child(1) > a'
psyc30 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(4) > div:nth-child(1) > ul > li:nth-child(1) > div > a'
psyc18 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(4) > div:nth-child(1) > ul > li:nth-child(4) > div > a'
psyc_102 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(4) > div:nth-child(2) > ul > li:nth-child(2) > div:nth-child(1) > a'
psyc_112 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(4) > div:nth-child(2) > ul > li:nth-child(2) > div:nth-child(3) > a'
psyc110 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(4) > div:nth-child(2) > ul > li:nth-child(3) > div:nth-child(1) > a'
psyc100w ='#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(6) > div:nth-child(1) > ul > li:nth-child(1) > div > a'
psyc154 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(6) > div:nth-child(1) > ul > li:nth-child(2) > div:nth-child(4) > a'
psyc129 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(6) > div:nth-child(1) > ul > li:nth-child(3) > div:nth-child(1) > a'
psyc118 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(6) > div:nth-child(2) > ul > li:nth-child(1) > div > a'
stat115 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(6) > div:nth-child(2) > ul > li:nth-child(2) > div:nth-child(4) > a'
psyc135 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(6) > div:nth-child(2) > ul > li:nth-child(3) > div:nth-child(3) > a'
psyc190 = '#table_block_n2_and_content_wrapper > table > tbody > tr:nth-child(2) > td.block_content_outer > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > div > div:nth-child(8) > div:nth-child(2) > ul > li:nth-child(1) > div:nth-child(1) > a'

psyc_1_intro_button_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/div[1]/ul/li[2]/div/table/tbody/tr/td/div[2]'
hist_15_content ='//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/div[1]/ul/li[5]/div[4]/table/tbody/tr/td/div[2]'
biol21_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/div[2]/ul/li[2]/div[1]/table/tbody/tr/td/div[2]/em[3]'
stat95_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/div[2]/ul/li[3]/div/table/tbody/tr/td/div[2]'
AFAM_2B_content ='//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/div[2]/ul/li[5]/div[1]/table/tbody/tr/td/div[2]'
psyc30_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[4]/div[1]/ul/li[1]/div/table/tbody/tr/td/div[2]'
psyc18_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[4]/div[1]/ul/li[4]/div/table/tbody/tr/td/div[2]'
psyc_102_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[4]/div[2]/ul/li[2]/div[1]/table/tbody/tr/td/div[2]'
psyc_112_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[4]/div[2]/ul/li[2]/div[2]/table/tbody/tr/td/div[2]'
psyc110_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[4]/div[2]/ul/li[3]/div[1]/table/tbody/tr/td/div[2]'
psyc100w_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[6]/div[1]/ul/li[1]/div/table/tbody/tr/td/div[2]'
psyc154_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[6]/div[1]/ul/li[2]/div[2]/table/tbody/tr/td/div[2]'
psyc129_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[6]/div[1]/ul/li[3]/div[1]/table/tbody/tr/td/div[2]'
psyc118_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[6]/div[2]/ul/li[1]/div/table/tbody/tr/td/div[2]'
stat115_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[6]/div[2]/ul/li[2]/div[2]/table/tbody/tr/td/div[2]'
psyc135_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[6]/div[2]/ul/li[3]/div[2]/table/tbody/tr/td/div[2]'
psyc190_content = '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[8]/div[2]/ul/li[1]/div[1]/table/tbody/tr/td/div[2]'

my_list = [psyc_1_intro_button, hist_15, biol21,stat95,AFAM_2B,psyc30, psyc_102, psyc_112, psyc110, psyc100w, psyc154, psyc129, psyc118, stat115, psyc135, psyc190]

my_list2 = [psyc_1_intro_button_content, hist_15_content, biol21_content,stat95_content,AFAM_2B_content,psyc30_content, psyc_102_content, psyc_112_content, psyc110_content, psyc100w_content, psyc154_content, psyc129_content, psyc118_content, stat115_content, psyc135_content, psyc190_content]

class browser:
    def __init__(self):
        self.browser = webdriver.Chrome(PATH)
        self.wait_five = WebDriverWait(self.browser, 5)
        self.parse = BeautifulSoup()
        
    def click_element(self):
        self.browser.get(psyc_ba_2021_2022_url)
        for i in my_list:
            time.sleep(0.3)
            self.wait_five.until(EC.element_to_be_clickable((By.CSS_SELECTOR, i))).click()
        return self.browser
    
    def get_content_dict(self):
        self.click_element()
        time.sleep(5)
        try:
            count =0
            my_dict = {}
            for i in my_list2:
                time.sleep(0.5)
                count+=1
                data = self.browser.find_element_by_xpath(i)
                html = data.get_attribute('outerHTML')
                attrs = BeautifulSoup(html, 'html.parser').text
                my_dict[attrs[:attrs.find('-')]] = attrs[attrs.find('-'):]
        except Exception as error:
            print(error)
            self.browser.quit()
        print(my_dict)
        self.browser.quit()
        
    def get_content(self):
        self.click_element()
        time.sleep(5)
        try:
            count =0
            for i in my_list2:
                time.sleep(0.5)
                count+=1
                data = self.browser.find_element_by_xpath(i)
                html = data.get_attribute('outerHTML')
                attrs = BeautifulSoup(html, 'html.parser')
                with open(course_description_data, 'a') as f:
                    f.write(f" \n{count}. {attrs.text}")
                print("\n>>> Sucessfully Extract content")
        except Exception as error:
            print(error)
            self.browser.quit()
        self.browser.quit()
        
    def get_whole_catalog_out_as_text_file(self):
        try:
            data = requests.get(whole_catalog_url)
            soup = self.parse(data, "html.parser")
            job_elements = soup.find_all("div", class_="acalog-core")
            with open('course_catalog.txt','w') as file:
                for job_element in job_elements:
                    file.write(job_element.text)
        except Exception as error:
            print(error)
            
    def get_whole_catalog_out_as_print(self):
        try:
            data = requests.get(whole_catalog_url)
            soup = self.parse(data, "html.parser")
            job_elements = soup.find_all("div", class_="acalog-core")
            for job_element in job_elements:
                print(job_element.text)
        except Exception as error:
            print(error) 
                       
if __name__ == '__main__':
    my_course = browser()
    my_course.get_content_dict()
    
        