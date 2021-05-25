import requests
from requests.auth import HTTPBasicAuth

# Naujo vartotojo registracija

# data = {'username': 'demo3', 'password': 'demo3'}
# r = requests.post('http://127.0.0.1:8000/signup', data=data)
# print(r.text)

# Įrašų atvaizdavimas su prisijungimu

# r = requests.get("http://127.0.0.1:8000/posts", auth=HTTPBasicAuth('demo2', 'demo2demo2'))
# print(r.text)


# Įrašų įrašymas su prisijungimu

# data = {'title': 'Straipsnis iš kliento programos', 'body': 'O čia straipsnio tekstas'}
# r = requests.post("http://127.0.0.1:8000/posts", auth=HTTPBasicAuth('demo2', 'demo2demo2'), data=data)
# print(r.text)


