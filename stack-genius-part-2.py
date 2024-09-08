from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd



import time

chrome_options = Options()

chrome_options.add_argument("--headless")

# Specify the file name
file_name = 'stack-genius-all-cards-urls.txt'

# Read the file content into a list
with open(file_name, 'r') as file:
    my_list = [line.strip() for line in file.readlines()]

# Print the list
print(my_list)
total_result = []
for index, list in enumerate(my_list):
    print("Index Number: ", index)
    result_dict = {}
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(list)
    # time.sleep(2)
    reject_cookie_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/div[2]/button[1]')
    reject_cookie_button.click()
    time.sleep(3)
    all_data_links = driver.find_element(By.XPATH, '/html/body/div[1]/main/header[1]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/div')
    all_links = all_data_links.find_elements(By.TAG_NAME,'a')
    get_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/header[1]/div/div/div/div[1]/div[1]/div[1]/div[2]/h2')
    result_dict['name'] = get_name.text
    for index, link in enumerate(all_links):
        result_dict[f'link {index}'] = link.get_attribute('href')
    print(result_dict)
    total_result.append(result_dict)

    driver.quit()


df = pd.DataFrame(total_result)
df.to_excel("stack-genius.xlsx", index=False)