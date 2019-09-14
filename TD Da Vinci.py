# install the requests package using 'pip3 install requests'
import requests

response = requests.post('https://api.td-davinci.com/api/simulants/search',
    headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiMGNlNjVjNjUtYWE3Zi0zNzYzLTg0MTUtNTdjM2RkMjllMDM1IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIxZDA3YTJhZC1hNTE0LTQ1ODItOGMxYi04ZGUyM2MyOWRmZTUifQ.Bf1LmnIBdvVKLia6bCmhV07TnQdzGwkbDcZBWQAzmLQ' })
response_data = response.json()

print(response_data)


