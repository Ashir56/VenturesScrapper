
import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://catalog.data.gov/dataset?q=&sort=metadata_created+desc")
# wait_for_page_load(driver)
driver.maximize_window()

time.sleep(10)

unordered_list = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/section[1]/div[2]/ul')

ordered_list = unordered_list.find_elements(By.CLASS_NAME, 'dataset-item')

total_result = []
for list in ordered_list:

    name_tag = list.find_element(By.CLASS_NAME, 'dataset-heading')
    anchor_tag = name_tag.find_element(By.TAG_NAME, 'a')

    views_tag = list.find_element(By.CLASS_NAME, 'recent-views-datagov')
    print(anchor_tag.text)
    print(views_tag.text)
    parent_div = list.find_element(By.CLASS_NAME, 'notes')
    second_div = parent_div.find_element(By.TAG_NAME, 'div')



    right_description = list.find_element(By.CLASS_NAME, 'dataset-organization').text

    print(right_description)

    print(second_div.text)

    total_result.append({'Name': anchor_tag.text, 'Views': views_tag.text, 'Description Header': right_description, 'Description Detail': second_div.text})


df = pd.DataFrame(total_result)
df.to_excel("data-gov.xlsx", index=False)
