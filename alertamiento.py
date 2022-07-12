import pandas as pd
import chardet
import os, fnmatch
import gzip
import shutil
import logging
logging.basicConfig(filename='SIS-BI-AlertamientoSOAT-CGB.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info('Inicio proceso de archivo de Alertamiento SOAT')
def findfile(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

try:
    with gzip.open(findfile('*.zip', './')[0], 'rb') as f_in:
        with open('CSB.csv', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
except Exception:
    logging.error('Error al extraer el archivo comprimido.')

try:    
    with open('CSB.csv', 'rb') as file_csv:
        result = chardet.detect(file_csv.read())  # or readline if the file is large
except Exception:
    logging.error('Error al extraer el archivo CSV.')



dforiginal = pd.read_csv('CSB.csv', encoding=result['encoding'], delimiter='|')
dfnombrebandeja = dforiginal.NombreBandeja.unique()
dfnombrerol = dforiginal.Rol.unique()
dfnombreestadopaquete = dforiginal.estado_paquete.unique()
print(dfnombrebandeja)