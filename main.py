import requests
url = "https://www.worldometers.info/coronavirus/#countries"
response = requests.get(url)

if response.status_code == 200:
    print("India")

else:
    print("Anurag")