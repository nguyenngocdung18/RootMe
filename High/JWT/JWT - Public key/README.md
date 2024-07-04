![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/77197ec4-6036-467b-a4e3-2c66cdc8a43f)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/61b9ad87-b826-4936-a643-a396fd6ac4b7)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/69ac87e7-59b1-46a9-ad5c-22a8fb5ff916)

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuKZ4DiQskg8q0lx8KDjj
T6XcWVxRV+sN2cta+DiTkaSeSbhR4m5O9zCUHaN6+xn/xMPU6qHc+qYjWxe0lPOq
Kx/SbUpKjJRoeaf3oXEoMM71rmLthZg5/WVbHs/1Kd1rOLdy0j9XVOJP+pzfPk6G
NFtBZwcElJXw1yf2qdjlQveiG9Zd/7iiUlFqr0bszQGNHKFTAPREArEU38KubHF/
HSOEOEJxNG3lCWv0Mryw04y36xYgJvIR0TDN3p4oFXucp6ysLeoBLv98WTOlKG+a
98ws5Z74T+gXTbD5sFTMjyr3Q1MP0xJQQgVfSqP98VmkM8uWBt11cM9FH6HoxD9a
OQIDAQAB
-----END PUBLIC KEY-----
```
không thể dùng username=admin được

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a09250da-f203-4b62-a07b-79815a47edaf)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c34bfb72-b742-48de-82d5-a56a7a9064a6)

Trong token này nó sẽ sử dụng private key để đăng kí và public key để verify

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/d468fc48-55e6-4a06-94a2-120c9c97794d)

Token JWT sẽ chia thành 3 phần header, payload, verify signature tương ứng với 3 màu. Giờ nếu ta trực tiếp sửa 
username dung thành admin thì sẽ bị lỗi vì vậy. ta copy riêng phần payload màu tím ra và sửa lại thành admin rồi
thay thế vào phần payload cũ

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/05c26ab2-cb28-4e10-8af3-0813d96cffec)

Tiếp theo sử dụng jwt_tool để tạo token

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/7ad8d2a3-f338-4063-83f0-ac7777e6080b)

file public.pem là file chứa public key

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/6b2deab9-eaad-46c9-a252-f5f08aa436bd)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/57819ee2-ee21-4e67-8f6b-d3318d1547e7)

=> HardcodeYourAlgoBro
