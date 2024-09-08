
import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.morningstar.com/best-investments")
driver.maximize_window()

time.sleep(6)

first_unordered_link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/section/div[3]/main/section/div[1]/section[2]/div/div[1]/ul')

ordered_lists = first_unordered_link.find_elements(By.CLASS_NAME, 'mdc-carousel-item__mdc')

print(len(ordered_lists))
total_result = []
for list in ordered_lists:
    header_tag = list.find_element(By.CSS_SELECTOR, '.mdc-heading__mdc.mdc-heading--level-6__mdc.mdc-heading--bold__mdc')
    print(header_tag.text)

    first_tag = list.find_elements(By.CSS_SELECTOR, '.mdc-locked-text__mdc.mdc-string')
    print(first_tag[0].text)
    print(first_tag[1].text)
    print(first_tag[2].text)

    print("==============================")

    total_result.append({'Header': header_tag.text, '1': first_tag[0].text, '2': first_tag[1].text, '3': first_tag[2].text})


df = pd.DataFrame(total_result)
df.to_excel("morningstar.xlsx", index=False)
