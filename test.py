import time
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.Chrome()

target_url: list[str] = ['http://sis-db-04/SOATReportConsole/InformesHistoricos/GeneradorInformes.aspx?Rpt=81']

# def aviso():
#     time.sleep(10)
#     driver.find_element(By.XPATH, '//*[@id ="exampleModal"]').send_keys(Keys.ESCAPE)


def loginpage():
    ui.WebDriverWait(driver, 10)
    driver.get("http://sis-db-04/SOATReportConsole/")
    # aviso()
    login = driver.find_element(By.XPATH, '//*[@id="txtuser"]')
    login.clear()
    login.send_keys("arruiz")
    time.sleep(2)
    pwd = driver.find_element(By.ID, "txtpassword")
    pwd.clear()
    pwd.send_keys("GWqT9h7HTz")
    driver.find_element(By.ID, "Button1").click()


def descargar():
    driver.get("http://sis-db-04/SOATReportConsole/InformesHistoricos/GeneradorInformes.aspx?Rpt=81")
    driver.implicitly_wait(10)
    fechaini = driver.find_element(By.ID, "Txtfecha_desde_textBox")
    time.sleep(2)
    fechaini.click()
    menumes = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_calendar"]/table/tbody/tr[1]/td[2]/span')
    menumes.click()
    time.sleep(2)
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[6]/td/span[1]')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[6]/td/span[1]')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[6]/td/span[1]')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[6]/td/span[1]')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/span')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[1]/span')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[2]/td/span[1]')
    menuslider.click()
    menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_calendar"]/table/tbody/tr[3]/td[6]')
    menuslider.click()
    fechafin = driver.find_element(By.ID, "TxtFecha_hasta_textBox")
    time.sleep(2)
    fechafin.click()
    fechahoy = driver.find_element(By.CLASS_NAME, "selectedCalendar")
    fechahoy.click()
    BotonDescarga = driver.find_element(By.XPATH, '//*[@id="BtnCsv"]')
    BotonDescarga.click()
    
    # fechaini.clear()
    # //*[@id="Txtfecha_desde_calendar"]/table/tbody/tr[1]/td[2]/span
    
    time.sleep(10)
    # fechainih = driver.find_element(By.ID, "Txtfecha_desde_hidden")
    # fechainih.send_keys("1/1/2022")
    # fechaini.click()
    # fechaini.clear()
    
    # time.sleep(2)
    # fechafin = driver.find_element(By.ID, "TxtFecha_hasta_textBox")
    # fechafin.clear()
    # fechafin.send_keys("31/12/2022")
    # time.sleep(20)
    

loginpage()
time.sleep(2)
descargar()
driver.quit()