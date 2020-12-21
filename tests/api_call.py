import requests

URL = "http://localhost:8080/predict"
FILE = {"image": open("../images/hat_selfies/hat1.jpg", 'rb')}
#FILE = {"image": open("../images/helmets/helmet1.jpg", 'rb')}
response = requests.post(url=URL, files=FILE)
print(response.json())