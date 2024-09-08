import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://finance.yahoo.com/markets/stocks/most-active/")
driver.maximize_window()

time.sleep(6)

table_body = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/section[2]/div/div/div/div/div/ul')

table_rows = table_body.find_elements(By.CLASS_NAME, 'stream-item')
print("Printing")
print(len(table_rows))

total_result = []

for row in table_rows:
    try:
        title = row.find_elements(By.CSS_SELECTOR, '.clamp.yf-1e4au4k')
        print(title[0].text)
        print(title[1].text)
        total_result.append({'Stocks Name': title[0].text, 'Stocks Description': title[1].text})
    except:
        print("Element not found")


df = pd.DataFrame(total_result)
df.to_excel("stocks-news.xlsx", index=False)
