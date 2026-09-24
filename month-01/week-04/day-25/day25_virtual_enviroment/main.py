import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

response.raise_for_status()

result = response.json()

print(result)
