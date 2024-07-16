import requests
from bs4 import BeautifulSoup
 
url = "http://challenge01.root-me.org/web-serveur/ch56/"

data = {
    "score": 1000000,
    "generate": "Give a try!"
}

# Thực hiện yêu cầu GET với header tùy chỉnh
response = requests.post(url, data = data)

strong_tags = BeautifulSoup(response.content, 'html.parser').find_all('strong')

print(strong_tags[1].text.strip())
