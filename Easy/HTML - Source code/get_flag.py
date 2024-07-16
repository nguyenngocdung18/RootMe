import requests

url = "http://challenge01.root-me.org/web-serveur/ch1/"

# Thực hiện yêu cầu GET tới URL
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Lấy nội dung trang
    content = response.text
    
    # Tìm flag
    start_index = content.find("password : ") + len("password : ")
    end_index = content.find("\n", start_index)
    flag = content[start_index:end_index].strip()
    
    # In flag
    print(f"The flag is: {flag}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
