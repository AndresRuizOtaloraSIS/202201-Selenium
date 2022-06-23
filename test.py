import time
from typing import List
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
logging.basicConfig(filename='SIS-BI-AlertamientoSOAT-CGB.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


driver = webdriver.Chrome()

target_url: list[str] = ['http://sis-db-04/SOATReportConsole/InformesHistoricos/GeneradorInformes.aspx?Rpt=81']

def loginpage():
    logging.info('Inicio proceso de descarga CGB')
    ui.WebDriverWait(driver, 10)
    driver.get("http://sis-db-04/SOATReportConsole/")
    login = driver.find_element(By.XPATH, '//*[@id="txtuser"]')
    login.clear()
    login.send_keys("arruiz")
    time.sleep(2)
    pwd = driver.find_element(By.ID, "txtpassword")
    pwd.clear()
    pwd.send_keys("GWqT9h7HTz")
    driver.find_element(By.ID, "Button1").click()


def descargar():
    try:
        driver.get("http://sis-db-04/SOATReportConsole/InformesHistoricos/GeneradorInformes.aspx?Rpt=81")
        driver.implicitly_wait(10)
    except Exception:
        logging.error('Error al conectar con consola de consulta.')
    try:
        fechaini = driver.find_element(By.ID, "Txtfecha_desde_textBox")
        time.sleep(2)
        fechaini.click()
        menumes = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_calendar"]/table/tbody/tr[1]/td[2]/span')
        menumes.click()
        time.sleep(2)
        anioinicial = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/span').get_attribute("innerHTML")
        while anioinicial != '2015':
            menuslider = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[6]/td/span[1]')
            menuslider.click()
            anioinicial = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/span').get_attribute("innerHTML")
        anio = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/span')
        anio.click()
        mesfechainicial = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[1]/span')
        mesfechainicial.click()
        diafechainicial = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_monthYear"]/div/table/tbody/tr[2]/td/span[1]')
        diafechainicial.click()
        aplicarfechainicial = driver.find_element(By.XPATH, '//*[@id="Txtfecha_desde_calendar"]/table/tbody/tr[3]/td[6]')
        aplicarfechainicial.click()
        fechafin = driver.find_element(By.ID, "TxtFecha_hasta_textBox")
        time.sleep(2)
        fechafin.click()
        fechahoy = driver.find_element(By.CLASS_NAME, "selectedCalendar")
        fechahoy.click()
        BotonDescarga = driver.find_element(By.XPATH, '//*[@id="BtnCsv"]')
        BotonDescarga.click()
        time.sleep(60)
    except:
        logging.error('Error al descargar el archivo de la consola de consultas')

loginpage()
descargar()
logging.info('Finaliza el proceso de descarga de CGB')
driver.quit()