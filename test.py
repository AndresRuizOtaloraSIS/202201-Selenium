import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium.webdriver.support.ui as ui

driver = webdriver.Firefox()
ui.WebDriverWait(driver, 10)
driver.get('https://prestadores.minsalud.gov.co/habilitacion/work.aspx')
time.sleep(20)
driver.find_element(By.XPATH, '//*[@id ="exampleModal"]').click()

