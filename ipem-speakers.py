from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

import time


driver = webdriver.Chrome()

driver.get("https://www.ipem-market.com/paris-2024/speakers/")
# wait_for_page_load(driver)
driver.maximize_window()



data_div = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div/div/section[2]/div[1]/div[2]/div/div/div[5]/div/div/div/div[1]')

elements = data_div.find_elements(By.CSS_SELECTOR, ".awsm-grid-list.awsm-grid-card.awsm-team-item.awsm-scale-anm.awsm-all")

total_result = []
for element in elements:
    element.click()
    time.sleep(4)
    data = data_div.find_element(By.CLASS_NAME, 'awsm-grid-show').text
    lines = data.split('\n')

    print(data)

    company = lines[0].strip() if len(lines) > 0 else ""
    name = lines[1].strip() if len(lines) > 1 else ""
    position = lines[2].strip() if len(lines) > 2 else ""

    total_result.append({'Company': company, 'Name': name, 'Position': position})


df = pd.DataFrame(total_result)
df.to_excel("ipem-paris-speakers.xlsx", index=False)

driver.quit()