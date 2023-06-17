import requests

path = "scan"
response = requests.get(url=f"http://localhost:8000/scan")

print(response)
