import requests
import pprint

url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/autocompletes"

querystring = {"query":"ho"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "4289f3c241msh83d99bd0356788dp1d9574jsnd0eb620ea0fb",
	"X-RapidAPI-Host": "crunchbase-crunchbase-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#NO FUNCIONA PARA QUE ME IMPRIMA ÚNICAMENTE LAS PALABRAS QUE ME INTERESAN.
"""for element in response["entities"]:
    print(element["identifier"]["value"])"""

pprint.pprint(response.json())