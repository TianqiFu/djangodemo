import datetime
import json
import requests

rqs_headers = {'Content-Type': 'application/json'}
req_url = 'http://localhost:8000/sensor/temperature_api'
new_data = {
    "captime": '',
    "captemperature": []
}

test_data = json.dumps(new_data)
print(test_data)
response = requests.post(url=req_url, data=test_data, headers=rqs_headers, verify=False)
print(response.text)
