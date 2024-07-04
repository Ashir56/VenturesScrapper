from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time

def wait_for_page_load(driver):
    timeout = 10  # Maximum wait time in seconds

    # Wait until the document state is 'complete'
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://app.folk.app/shared/All-companies-2mideB7XWyZzKRCr0w0Ydw6TZsu2ekkB')
wait_for_page_load(driver)
driver.maximize_window()

time.sleep(10)


element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[3]')
loaded_elements = list()
while True:
    company_divs = element.find_elements(By.CLASS_NAME, 'c-bxgLFE')
    new_data_loaded = False

    for div in company_divs:
        index = div.get_attribute('aria-rowindex')
        try:
            company = div.find_element(By.CSS_SELECTOR, '.c-gZNEbh.c-jxvbnT.c-gZNEbh-drVgRi-variant-textMedium.c-gZNEbh-iepcqn-truncate-true')
        except Exception as e:
            continue

        # element_key = (index, company.text)
        if company.text not in loaded_elements:
            print(index, company.text)
            loaded_elements.append(company.text)
            new_data_loaded = True



    # driver.execute_script("window.scrollBy(0, 10000);")


    # driver.execute_script("window.scrollBy(0,100000)", "")
    # Scroll vertically within the table
    table_element = driver.find_element(By.CLASS_NAME, 'c-cPjCsh')
    driver.execute_script("arguments[0].scrollTop += 300", table_element)

    time.sleep(5)
    if new_data_loaded is False:
        break


driver.quit()
