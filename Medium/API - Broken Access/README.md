![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/9b54f3fe-2611-4c0d-8346-212d5a867c9e)

Bắt được request này và chuyển nó tới Burp Suite

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/aaa97862-5702-4719-a876-48ef53ce133e)

Sử dụng "Change request method" 
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a6e87e7f-f12c-4d35-bc3a-ce8fcc07722e)

Đổi thành /api/signup

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/ba1dd5c4-f7c9-409c-b53a-5a5c97240a56)

Sửa Content-Type: application/json

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/e021510f-290b-494d-8eeb-04f5690a6f76)

=> Tạo account thành công

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/210b3891-3cac-4660-9d10-49afd6f438b2)

=> Đăng nhập thành công . có được session cookie. Sử dụng "Change request method" và session cookie vừa có được, ta có thể thấy userid của tài khoản vừa tạo là 2

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c5950ee7-bc99-4781-a4c0-5ed6a9200746)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/b2ccfb15-a3a0-4cb1-8a5c-dffedcd2717e)

Và tôi thử với path ```/api/user/1```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/6572ccbe-5376-4b81-af14-82334523e4f1)

=> flag: RM{E4sy_1d0r_0n_API}
