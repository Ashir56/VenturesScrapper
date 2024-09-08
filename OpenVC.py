from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.openvc.app/country/France")
driver.maximize_window()

whole_table = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[3]/div/div[4]/table/tbody')
whole_table_data = whole_table.find_elements(By.TAG_NAME, 'tr')

required_classes = 'sponsorRow sponsorRow2 adType_1'

for table_data in whole_table_data:
    tr_classes = table_data.get_attribute('class')
    if all(cls in tr_classes for cls in required_classes.split()):
        print("The <tr> element has the required CSS classes.")
        continue

    element = table_data.find_element(By.CLASS_NAME, 'nameCell')

    print(element)


    # name = element.find_element(By.ID, 'invOverflow').text
    # print(name)
