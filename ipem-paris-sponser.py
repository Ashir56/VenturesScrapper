from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

import time


driver = webdriver.Chrome()

driver.get("https://www.ipem-market.com/paris-2024/sponsors-and-partners/")
# wait_for_page_load(driver)
driver.maximize_window()

sponsors_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div/div/section[3]/div[2]/div/div/div/div/div/div/div')
time.sleep(4)
sponsors_links = sponsors_element.find_elements(By.TAG_NAME, "a")

sponsors_urls = [a.get_attribute("href") for a in sponsors_links]

df = pd.DataFrame({'Urls': sponsors_urls})

df.to_excel("ipem-paris-sponsors.xlsx", index=False)


industry_sponsors = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div/div/section[5]/div[2]/div/div/div/div/div/div/div')
time.sleep(4)

industry_sponsors_links = industry_sponsors.find_elements(By.TAG_NAME, "a")

industry_sponsors_urls = [a.get_attribute("href") for a in industry_sponsors_links]

df = pd.DataFrame({'Urls': industry_sponsors_urls})

df.to_excel("ipem-paris-industry-supporter.xlsx", index=False)

media_supporter = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div/div/section[6]/div[2]/div/div/div/div/div/div/div')
time.sleep(4)

media_supporter_links = media_supporter.find_elements(By.TAG_NAME, "a")

media_supporter_urls = [a.get_attribute("href") for a in media_supporter_links]


df = pd.DataFrame({'Urls': media_supporter_urls})

df.to_excel("ipem-paris-media-supporter.xlsx", index=False)



