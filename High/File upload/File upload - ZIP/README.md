![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/ce2bf1ae-add2-4dcb-8f1a-13109ec8477c)

Tạo 1 file rồi nén zip và upload

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a88d8cc1-7538-430f-9b5f-08fcc3790ec4)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/542160f8-2354-45e5-9ad9-dbb12f0019e6)

Ta thấy file đã được unzip lại thành exploit.txt. Và vì ta đang cần đọc source code của file index.php mà từ URL hiện tại, ta có thể xác định được vị trí của file là ../../../index.php

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a91ac6aa-8fd3-45e5-a858-20b479810476)

Trên HackTricks, tôi tìm thấy 1 vector có thể khai thác bằng việc symlink

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/aea0cea0-692d-4722-86c0-10512fbee948)

tiến hành symlink rồi nén zip và upload lại file.

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c2701293-18bb-4a04-b4f7-6897084f56be)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/151628ab-dfd3-4b25-8c2b-031712278079)


![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/e4976f7a-ace3-41c5-8c5c-56d9b72f6485)

Click để xem file index.txt ( giờ nó đã được symlink với index.php)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/931abeaa-0aab-401b-9db0-ec288a4e7bc0)

=> N3v3r_7rU5T_u5Er_1npU7
