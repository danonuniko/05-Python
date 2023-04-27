import requests

"""	
Se usan estas líneas para no utilizar el valor exacto de la api_key cuando el objetivo es subir la información a un repositorio remoto.
No me termina de funcionar.

import os
openai.api_key = os.getenv("RAPID_API")
"""

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

text = input("Introduce un texto en español: ")

payload = {
	"q": text,
	"target": "en",
	"source": "es"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key":  "4289f3c241msh83d99bd0356788dp1d9574jsnd0eb620ea0fb",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json()["data"]["translations"][0])