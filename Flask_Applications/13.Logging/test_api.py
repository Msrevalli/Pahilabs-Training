import requests

# Define the URL of the API endpoint
url = 'http://127.0.0.1:5000/process-data'

# Valid JSON data
data = {
    'value': 10
}

# Make a POST request
response = requests.post(url, json=data)

# Print the response
print('Status Code:', response.status_code)
print('Response JSON:', response.json())
