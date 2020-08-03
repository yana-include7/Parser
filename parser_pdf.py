from selenium.webdriver import Chrome
from selenium import webdriver
import os
import pandas as pd
import re
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
from tqdm import tqdm
import argparse

def t_o():
    time.sleep(random.uniform(5.5, 9.5))

absdwdirname = os.path.abspath('test')
chromeOptions = Options()
prefs = {"download.default_directory" :absdwdirname}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chromeOptions)

driver.get("https://egrul.nalog.ru/index.html")
DATA = os.listdir('test')

def download_pdf(name):
    try:
        search = driver.find_element_by_id('query')
        search.clear()
        search.send_keys(name)
        S = driver.find_element_by_id('btnSearch')
        S.click()
        t_o()
        ress = driver.find_elements_by_class_name("res-row")
        if ress:
            try:
                b = ress[0].find_element_by_tag_name("button")
                b.click()
                t_o()
            except Exception as E:
                print(E)
        else:
            pass
    except:print("Превышен лимит запросов! ")
