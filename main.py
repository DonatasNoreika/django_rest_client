import requests
from requests.auth import HTTPBasicAuth
#
# requests.get(
#   'https://api.github.com/user',
#   auth=HTTPBasicAuth('admin', 'admin')
# )

r = requests.get("http://127.0.0.1:8000/posts", auth=HTTPBasicAuth('demo2', 'demo2demo2'))

print(r.text)
