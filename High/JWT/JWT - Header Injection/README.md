![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/7bb3556c-2c33-4b00-a2f6-7b1831abd9cc)

Cần phải có key để đăng nhập

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/be95bd72-d5c7-46e7-ab72-08bd6a912558)

thử decode cái ví dụ 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/7c2aaf37-4162-4d87-992d-134d20e5fad5)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f53b2110-e72a-448b-8ecb-b8469c9db901)

Chỉ user Neo mới vào được

+ Sử dụng Burp Suite extension "JWT Editor Keys" và tạo private key bằng "New RSA key"
+ Sau đó dùng extension "JSON Web Token" Và ấn Attack -> Embedded JWK để nhúng 

=> Tạo được 1 token sau:
```
eyJraWQiOiJiZDFlMDZmYy03YTBhLTQ5MWUtYjU1MC02YWYxMTQ4MTRjMmIiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsImtpZCI6ImJkMWUwNmZjLTdhMGEtNDkxZS1iNTUwLTZhZjExNDgxNGMyYiIsIm4iOiJsd2lUNWhUOVhPOHptaVRoRW5BX3A0aWtqblUxZkJyV2tYVWNTRVRwT19DNWZEeHl1dmVIV1A1T1NpdG4tbjNXME9SSUFWMHlTeW9ZeVhEZnFSMFloZGFiZk16WHR2cnB1b1BucXlPRGpMUHBvR1lJSFV4MGhHekdNajlPbFFMQl9pNTF6ZENGWF9JNXF5bEhPUndiNXhKcUNMcUhCUU5JakFPUjRPM1czSF8wdGZhaGhtT29fblVLRFFob3NMblFNc2N1bGZYUDZvVmFfOHZpWVZKNDAwSTdVemxqYzRTSElzb0lUUnZFR0FjTVRaRFZXd3o2NmZ2QTlJZ3FLa3V1YnVVV293OU5yTE9wTDdxM1RaYU12UzJ3NWI3TnQwMTlOaDA3bnRXcDE4RjlQRG9NT0dWVVdXVTJ0UXlMTVRXX0dQMnp1aDRyMXFFSVNVMXhGWGU5MFEifX0.eyJ1c2VyIjoiTmVvIiwiaWF0IjoxNjc2NjM3ODMyfQ.M0n_hBVOnzi-j751yiqzUmhVCPLxhrVZX4lK6Tfyc34Nm_-3gTYeKOwOtecb8CbYgjz6nWnbVQIIKleeSsVNcIlfYH8e1n2wJ6JAyNvqCCHHA5W7dzWX9hnZ0tiRSLNurNAutp-ghYjTfQouTZc4MyLAwx00YqsQtiCKQQqBXXOXq8A5-vhdPWp7czxy8LT1C5GqM7dWBsyeFZMHa5a-l4wVKmHvKZunG0PWxr1p6xPsZ5DTgPWyexPITjreiGJoEKCXmr5beUAnzu2Q29YA6s_XLNoUUSp6B6O5W_iGPPez8cSLZhmnK-knOqa7Wof6kK3Q33e6d4CBtgnyEtV4_w
```
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c43b96e5-4b3b-496e-8fcd-4741bef405be)
