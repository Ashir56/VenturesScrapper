import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://ieeexplore.ieee.org/abstract/document/7943218/citations#citations")
driver.maximize_window()

time.sleep(6)

element_tab = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[3]/div/xpl-root/main/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/xpl-accordian-section/div/xpl-document-accordion/div[3]/div[2]/xpl-all-citation/section/div[2]/div[2]')


row_tabs = element_tab.find_elements(By.CLASS_NAME, 'reference-container')

total_result = []

for row in row_tabs:
    description = row.find_element(By.CLASS_NAME, 'description').text
    print(description)
    article = row.find_element(By.CLASS_NAME, 'stats-citations-link-viewArticle')
    scholar = row.find_element(By.CLASS_NAME, 'stats-citations-link-googleScholar')
    article_link = article.get_attribute('href')
    scholar_link = scholar.get_attribute('href')

    print(article_link)
    print(scholar_link)
    print("===============")

    total_result.append({'Description': description, 'Article': article_link, 'Scholar': scholar_link})


df = pd.DataFrame(total_result)
df.to_excel("ieeexplore.xlsx", index=False)
