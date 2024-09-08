import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.kayak.com/packages/United-States-U253/2024-09-19/2024-09-26/-1,-1/2/0,0,0/LHE?sort=rank_a")
# wait_for_page_load(driver)
driver.maximize_window()

time.sleep(10)


cards_div = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[3]/div[2]')


cards = cards_div.find_elements(By.CSS_SELECTOR, 'div.iRhY')

total_result = []
for card in cards:
    name = card.find_element(By.CLASS_NAME, 'BN7K-link').text
    rating = card.find_element(By.CLASS_NAME, 'Ius0').text
    # rate_text = card.find_element(By.CLASS_NAME, 'gQtw').text
    # rate_rating = card.find_element(By.CLASS_NAME, 'gQtw-rating').text
    price = card.find_element(By.CLASS_NAME, 'LR-R-best').text
    price_total = card.find_element(By.CLASS_NAME, 'LR-R-total-price').text
    _type = card.find_element(By.CLASS_NAME, 'LR-R-type').text
    # meals_type = card.find_element(By.CLASS_NAME, 'LR-R-board-type').text

    print(name)
    print(rating)
    print(price)
    total_result.append({'Name': name, 'Rating': rating, 'Price': price, 'Type': _type})




df = pd.DataFrame(total_result)
df.to_excel("kayak.xlsx", index=False)


driver.quit()