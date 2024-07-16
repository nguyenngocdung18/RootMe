import requests
from bs4 import BeautifulSoup

url = "http://challenge01.root-me.org/web-serveur/ch68/"

headers = {
    "X-Forwarded-For": "192.168.1.1"
}

# Thực hiện yêu cầu GET với header tùy chỉnh
response = requests.get(url, headers=headers)

print(BeautifulSoup(response.content, 'html.parser').find('strong').text)
