![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/399c1515-2215-4ef6-a45b-40e68f2499fb)

Click vào "Login a guest" ta có được 1 cookie 
```jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/8d0c86ae-469c-4b05-beb8-1a4aba5ef59a)

decode 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/8ccf21b6-0c7b-4d25-8afd-c0f52dd41fe2)

Theo tài liệu thì ta sẽ thử đổi HS256 thành none

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f13c38bd-59f6-4c0f-b005-6b06f3ce3337)

Sử dụng CyberChef để decode từng phần của cookie

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/d6ae8e35-439e-4e10-8c31-1fcf81e56140)

Sửa HS256 -> none và tiến hành encode với base64

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a497db94-8486-4d8d-b699-7d17b2b6ed85)

Tiếp tục làm tương tự

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/112af317-7934-44c7-bfc7-32c500a9e6ee)

Chuyển guest -> admin và encode

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/506da8c1-e0c4-4e6e-865f-72447f215dce)

Giờ ta chỉ cần thêm phần cuối vào và gửi đi =))) tada. 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/81b5e7e9-f5eb-4ae2-9eb1-ce13eb26ad58)

=> S1gn4tuR3_v3r1f1c4t10N_1S_1MP0Rt4n7
