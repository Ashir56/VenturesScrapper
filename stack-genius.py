from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import time


driver = webdriver.Chrome()

driver.get("https://www.stackgenius.io/solutions")
driver.maximize_window()

time.sleep(3)

reject_cookie_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[3]/div[2]/button[1]')
reject_cookie_button.click()
all_links_to_scrap = []
time.sleep(3)
while True:
    try:
        # show_more_button = driver.find_element(By.CSS_SELECTOR,
        #                                        'a.w-pagination-next.button-ghost')

        show_more_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.w-pagination-next.button-ghost'))
        )

        show_more_button.click()
        print("Button Clicking========!!!!")
        time.sleep(3)

    except TimeoutException:
        print("Out of the loop")
        break

time.sleep(5)


cards_list = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/section/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div[1]')
card_divs = cards_list.find_elements(By.ID, 'w-node-b95889c8-f34f-27c5-8a2a-f63ae74055e2-3e72ddbc')

for div in card_divs:
    link_tag = div.find_elements(By.TAG_NAME, 'a')
    print(link_tag[0].get_attribute('href'))
    with open('stack-genius-all-cards-urls.txt', 'a') as file:
        file.write(f"{link_tag[0].get_attribute('href')}\n")
print(len(card_divs))
print("Ending the program")





