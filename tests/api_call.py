import requests

URL = "http://localhost:8080/api"
FILE = {"image": open("hat_selfies/hat1.jpg", 'rb')}
response = requests.post(url=URL, files=FILE)
for label in response.json()['code']:
    print(label['Name'] + ' : ' + str(label['Confidence']))