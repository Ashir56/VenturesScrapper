from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd

import time

# def wait_for_page_load(driver):
#     timeout = 10  # Maximum wait time in seconds
#
#     # Wait until the document state is 'complete'
#     WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
#     WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
# service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get("https://app.folk.app/shared/All-US-Family-Offices-MmIn8iedXIvLRqSdkdwZOguMsOnOw6dA")
# wait_for_page_load(driver)
driver.maximize_window()

time.sleep(15)


element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[3]')

loaded_elements = list()
final_data = []
table_headers_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/div')
table_headers_divs = table_headers_element.find_elements(By.CLASS_NAME, 'c-crGDbs')
table_headers_data = []

for table_div in table_headers_divs:
    table_headers_data.append(table_div.text)
while True:
    company_divs = element.find_elements(By.CLASS_NAME, 'c-bxgLFE')
    new_data_loaded = False
    row_divs = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div')
    row_divs = row_divs.find_elements(By.XPATH, "//div[@role='row']")

    for div in company_divs:
        index = div.get_attribute('aria-rowindex')
        try:
            company = div.find_element(By.CSS_SELECTOR, '.c-gZNEbh.c-jxvbnT.c-gZNEbh-drVgRi-variant-textMedium.c-gZNEbh-iepcqn-truncate-true')
        except Exception as e:
            continue

        # element_key = (index, company.text)
        if company.text not in loaded_elements:
            data = {}
            for row_div in row_divs:
                row_index = row_div.get_attribute('aria-rowindex')
                if row_index == index:
                    contents = row_div.find_elements(By.CLASS_NAME, 'c-kvDAVN')
                    print(index, company.text)
                    data['index'] = index
                    data['company'] = company.text
                    for i, content in enumerate(contents):
                        data[table_headers_data[i]] = content.text
                    loaded_elements.append(company.text)
                    new_data_loaded = True
                    final_data.append(data)



    # driver.execute_script("window.scrollBy(0, 10000);")


    # driver.execute_script("window.scrollBy(0,100000)", "")
    # Scroll vertically within the table
    table_element = driver.find_element(By.CLASS_NAME, 'c-cPjCsh')
    driver.execute_script("arguments[0].scrollTop += 400", table_element)

    time.sleep(12)
    if new_data_loaded is False:
        break

print("============================================")
print("Final Data")
print("Length : ", len(final_data))

df = pd.DataFrame(final_data)
df.to_excel("us-family-offices.xlsx", index=False)

driver.quit()
