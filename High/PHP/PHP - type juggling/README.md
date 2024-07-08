![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/b4b0eeac-15ff-4fba-a9b3-399b863694bc)

Khi tôi thử với account admin:admin thì trong http request được mã hóa thành như ảnh bên dưới

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/4b04d03e-7267-459b-9c34-873bd08f4954)

xem source code

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/87bfbc25-988c-414e-b794-10205eb88a9f)

Vì $auth được gọi bằng json_decode nên nó sẽ trả về dạng chuỗi ví dụ như là

```
$auth = [
    "username" => "exampleUser",
    "password" => "examplePasswordHash"
];
```

```
if($auth['data']['login'] == $USER && !strcmp($auth['data']['password'], $PASSWORD_SHA256)){
        $return['status'] = "Access granted! The validation password is: $FLAG";
    }
```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/d4a5aebb-3d4d-492a-8a46-7b659c2d8a08)

Ngoài ra, tôi còn tìm hiểu được nó cũng sẽ Returns 0 nếu ta truyền vào một array thay vì một string, 
kể cả khi warning (‘WARNING strcmp() expects parameter 2 to be string, array given on line number …!’) xuất hiện. 

Vì vậy tôi sửa lại payload admin = 0  để lợi dụng Loose Comparison 0 == chuỗi => TRUE 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c36fd014-2802-49cf-9047-92dcf845d809)

=> DontForgetPHPL00seComp4r1s0n
