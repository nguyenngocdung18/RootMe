import requests

url = "http://challenge01.root-me.org/web-serveur/ch1/"

# Thực hiện yêu cầu GET tới URL
response = requests.get(url)

# Lấy nội dung trang
content = response.text
    
# Tìm flag
start = content.find("password : ") + len("password : ")
end = content.find("\n", start)
flag = content[start:end].strip()
    
# In flag
print(f"The flag is: {flag}")

