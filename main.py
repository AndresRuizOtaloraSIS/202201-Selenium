# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.Firefox()

def loginpage():
    ui.WebDriverWait(driver, 10)
    driver.get('https://prestadores.minsalud.gov.co/habilitacion/work.aspx')
    login = driver.find_element(By.XPATH, '//*[@id="tbid_usuario"]')
    login.clear()
    login.send_keys("invitado")
    time.sleep(2)
    pwd = driver.find_element(By.ID, "tbcontrasena")
    pwd.clear()
    pwd.send_keys("invitado")
    driver.find_element(By.ID, "Button1").click()
def prestadorespage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/habilitados_reps.aspx?pageTitle=Registro%20Actual&pageHlp=')
    driver.find_element(By.ID, "_ctl0_ibBuscarFtr").click()
    try:
        element = WebDriverWait(driver, 240).until(
            EC.presence_of_element_located((By.ID, "_ctl0_ContentPlaceHolder1_lblnregs"))
        )
    finally:
        try:
            element = WebDriverWait(driver, 240).until(
                EC.presence_of_element_located((By.ID, "_ctl0_ContentPlaceHolder1_ibExcel"))
            )
        finally:
            time.sleep(20)
            driver.find_element(By.ID, "_ctl0_ContentPlaceHolder1_ibExcel").click()
        time.sleep(60)
loginpage()
prestadorespage()
driver.quit()

#//*[@id="_ctl0_ContentPlaceHolder1_btn_sedes_reps"]