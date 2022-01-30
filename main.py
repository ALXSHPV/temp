import requests
from pprint import pprint
url = 'https://api.github.com/user/repos'
username = 'ALXSHPV'
token ="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"
response = requests.get(url, auth=(username, token))
j_data = response.json()
print(type(j_data))

