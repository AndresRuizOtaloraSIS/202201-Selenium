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

target_url: list[str] = ['https://prestadores.minsalud.gov.co/habilitacion/consultas/habilitados_reps.aspx',
                  'https://prestadores.minsalud.gov.co/habilitacion/consultas/sedes_reps.aspx',
                  'https://prestadores.minsalud.gov.co/habilitacion/consultas/serviciossedes_reps.aspx',
                  'https://prestadores.minsalud.gov.co/habilitacion/consultas/capacidadesinstaladas_reps.aspx',
                  'https://prestadores.minsalud.gov.co/habilitacion/consultas/medidasseguridad_reps.aspx',
                  'https://prestadores.minsalud.gov.co/habilitacion/consultas/sanciones_reps.aspx']

def aviso():
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id ="exampleModal"]').send_keys(Keys.ESCAPE)


def loginpage():
    ui.WebDriverWait(driver, 10)
    driver.get("https://prestadores.minsalud.gov.co/habilitacion/work.aspx")
    aviso()
    login = driver.find_element(By.XPATH, '//*[@id="tbid_usuario"]')
    login.clear()
    login.send_keys("invitado")
    time.sleep(2)
    pwd = driver.find_element(By.ID, "tbcontrasena")
    pwd.clear()
    pwd.send_keys("invitado")
    driver.find_element(By.ID, "Button1").click()


def descargar(url):
    driver.get(url)
    driver.find_element(By.ID, "_ctl0_ibBuscarFtr").click()
    try:
        WebDriverWait(driver, 240).until(
            ec.presence_of_element_located((By.ID, "_ctl0_ContentPlaceHolder1_lblnregs"))
        )
    finally:
        try:
            WebDriverWait(driver, 240).until(
                ec.presence_of_element_located((By.ID, "_ctl0_ContentPlaceHolder1_ibExcel"))
            )
        finally:
            time.sleep(20)
            driver.find_element(By.ID, "_ctl0_ContentPlaceHolder1_ibExcel").click()
        time.sleep(10)


loginpage()
for n in range(len(target_url)):
    descargar(target_url[n])
time.sleep(50)
driver.quit()