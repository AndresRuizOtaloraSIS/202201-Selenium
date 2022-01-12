# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.Chrome()


def aviso():
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id ="exampleModal"]').click()


def loginpage():
    ui.WebDriverWait(driver, 10)
    driver.get('https://prestadores.minsalud.gov.co/habilitacion/work.aspx')
    aviso()
    login = driver.find_element(By.XPATH, '//*[@id="tbid_usuario"]')
    login.clear()
    login.send_keys("invitado")
    time.sleep(2)
    pwd = driver.find_element(By.ID, "tbcontrasena")
    pwd.clear()
    pwd.send_keys("invitado")
    driver.find_element(By.ID, "Button1").click()


def descargar():
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


def prestadorespage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/habilitados_reps.aspx')
    descargar()


def sedespage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/sedes_reps.aspx')
    descargar()


def serviciospage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/serviciossedes_reps.aspx')
    descargar()


def capacidadpage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/capacidadesinstaladas_reps.aspx')
    descargar()


def medidasseguridadpage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/medidasseguridad_reps.aspx')
    descargar()


def sancionespage():
    driver.get(
        'https://prestadores.minsalud.gov.co/habilitacion/consultas/sanciones_reps.aspx')
    descargar()


loginpage()
prestadorespage()
sedespage()
serviciospage()
capacidadpage()
medidasseguridadpage()
sancionespage()
time.sleep(50)
driver.quit()
