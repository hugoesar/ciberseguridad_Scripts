# Usar la API de Have I been pwn?
import requests
import json
import logging
import getpass

apikey = getpass.getpassgetpass(input("Ingresa el apikey"))
headers = {}
headers['content-type']= 'application/json'
headers['api-version']= '3'
headers['User-Agent']='python'
#Place that API key here
headers['hibp-api-key']=apikey
#Preguntar correo a revisar
email = input("Ingrese el correo a investigar")#'falso@hotmail.com'
#solicitud
url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
        email+'?truncateResponse=false'
r = requests.get(url, headers=headers)
if r.status_code == 200:
    data = r.json()
    encontrados = len(data)
    if encontrados > 0:
        print("Los sitios en los que se ha filtrado el correo",email,"son:")
        for filtracion in data:
            etpassnombre = filtracion.get("N", "Desconocido")
            fecha_filtracion = filtracion.get("fecha", "Desconocida")
            dominio = filtracion.get("Dominio", "No disponible")
            reporte = """
            corre(f"Nombre del correo: {email}"
            print(f"\nNombre de la filtración: {nombre}")
            print(f"Fecha de la filtración: {fecha_filtracion}")
            print(f"Dominio afectado: {dominio}")
            """
            with open('reporte_filracionemail.txt','w') as file:
                file.write(reporte)
    else:
        print("El correo",email,"no ha sido filtrado")
    for filtracion in data:
        print(filtracion["Name"])
    msg = email+" Filtraciones encontradas: "+str(encontrados)
    print(msg)
    logging.basicConfig(filename='hibpINFO.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p",
                        level=logging.INFO)
    logging.info(msg)
else:
    msg = r.text
    print(msg)
    logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
    logging.error(msg)
