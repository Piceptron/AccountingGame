# install the requests package using 'pip3 install requests'
import requests
import os

response = requests.post('https://api.td-davinci.com/api/simulants/search',
    headers = { 'Authorization':os.environ.get('key')})
response_data = response.json()

customer_id = response_data['result']['customers'][0]['id']

output = response_data['result']['customers'][0]['givenName'] + '\n'
output += response_data['result']['customers'][0]['surname'] + '\n'
output += '' + str(response_data['result']['customers'][0]['totalIncome']) + '\n'

print(output)
