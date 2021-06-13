import re
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class GETAJOB:
    def __init__(self, keyword, area, page, username, password, intro_idx):
        self.keyword = keyword
        area_num = ""
        for number in area:
            area_num += str(number)
            area_num += "%2C"
        self.area_num = area_num
        self.page = page
        self.username = username
        self.password = password
        self.intro_idx = intro_idx
    def _get_all_submit_url(self):
        all_submit_url = []
        pattern = r".+/(.+)\?.+"
        headers = {"Referer": "https://www.104.com.tw/jobs/search/?ro=0&keyword=python%20&expansionType=area,spec,com,job,wf,wktm&jobsource=2018indexpoc"}
        for p in range(1, self.page+1):
            data = requests.get(f"https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword={self.keyword}%20&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area={self.area_num}&order=12&asc=0&page={p}&mode=s&jobsource=2018indexpoc", headers=headers).json()
            data = data["data"]
            if data["list"]:
                for single_job in data["list"]:
                    job_url = single_job["link"]["job"]
                    cust_url = single_job["link"]["cust"]
                    job = re.findall(pattern, job_url)[0]
                    cust = re.findall(pattern, cust_url)[0]
                    if job and cust:
                        url = f"https://m.104.com.tw/apply/step1/{cust}/{job}?jobsource=m104"
                        all_submit_url.append(url)
        return all_submit_url
    
    def submit_job(self, all_submit_url):
        driver = webdriver.Chrome(".\chromedriver.exe")
        driver.get(all_submit_url[0])
        sleep(2)
        id_code = driver.find_element_by_id("username")
        id_code.send_keys(self.username)
        sleep(1)
        password = driver.find_element_by_id("password")
        password.send_keys(self.password)
        sleep(1)
        login = driver.find_element_by_id("submitBtn")
        login.click()
        sleep(3)
        try:
            select = Select(driver.find_element_by_id("applyCover"))
            select.select_by_index(self.intro_idx)
            sleep(1)
            submit = driver.find_element_by_class_name("submit")
            submit.click()
        except:
            pass
        for idx in range(1, len(all_submit_url)):
            driver.get(all_submit_url[idx])
            sleep(0.5)
            try:
                select = Select(driver.find_element_by_id("applyCover"))
                select.select_by_index(self.intro_idx)
                sleep(0.5)
                submit = driver.find_element_by_class_name("submit")
                submit.click()
            except:
                pass


