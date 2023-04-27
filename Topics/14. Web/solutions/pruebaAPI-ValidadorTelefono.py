import requests
import pprint

url = "https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp"

telefono = input("Introduce un teléfono: ")
querystring = {"number":telefono}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "4289f3c241msh83d99bd0356788dp1d9574jsnd0eb620ea0fb",
	"X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pprint.pprint(response.json())