from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

import time
driver = webdriver.Chrome()

driver.get("https://www.seedtable.com/investors-france")

header_list = driver.find_element(By.XPATH, '/html/body/main/section[2]/div')

total_elements = header_list.find_elements(By.CSS_SELECTOR, 'div.bg-white.text-black.border.border-gray-200.rounded-lg.shadow-md.p-4.my-4.md\:p-6.md\:flex')

print(len(total_elements))

result = []


for element in total_elements:
    result_data = {}
    header = element.find_element(By.CSS_SELECTOR, '.text-xl.font-bold.text-black.hover\\:text-blue-500').text
    website = element.find_element(By.CSS_SELECTOR, '.text-sm.text-gray-600.hover\\:underline').text
    description = element.find_element(By.CSS_SELECTOR, '.text-sm.overflow-hidden').text

    right_side_of_the_card = element.find_element(By.CSS_SELECTOR, '.md\\:w-2\\/3.md\\:pl-4')
    contents = right_side_of_the_card.find_elements(By.CSS_SELECTOR, '.overflow-hidden.p-3.rounded-lg')
    result_data['title'] = header
    result_data['website'] = website
    result_data['description'] = description
    for content in contents:
        title = content.find_element(By.CSS_SELECTOR, '.font-normal.font-mono.font-xs.text-gray-600').text

        title_contents = content.find_elements(By.CSS_SELECTOR, '.text-sm.mb-1')
        if len(title_contents) <= 0 :
            title_contents = content.find_elements(By.CSS_SELECTOR, '.text-sm')
        empty_string = ''
        for data in title_contents:
            empty_string += data.text
            empty_string += ', '

        result_data[title] = empty_string

    result.append(result_data)

df = pd.DataFrame(result)
df.to_excel("seedtable.xlsx", index=False)
