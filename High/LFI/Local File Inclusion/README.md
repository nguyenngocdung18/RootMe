![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/5269215a-0be6-4c97-84d8-ae32b695fd0c)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/9e451ad7-204a-4ed6-867f-58c2fbdccddf)

Từ URL ta có thể đoán thư mục cha mà ta "đang đứng" sẽ là files=sysadm còn các tệp con sẽ là f=index.html

Giờ ta sẽ thử đi đọc tệp index của admin. Khi ấn vào admin thì nó chuyển tới đường dẫn /admin

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c0251d29-f7de-4f58-a853-1e70193e8b29)

Sau khi thử một vài  payload như là ../ hoặc .../ thì chỉ lên được 1 cấp mà không có file gì để đọc còn nếu
tiếp tục ../../ hoặc .../.../ thì sẽ bị lỗi.

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/8551ec63-bea9-40ba-9082-0272ed47cf0e)

tôi đã tìm thấy payload có thể escape là ..//..//

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/645d5f4a-bf5d-4098-9ca3-9afb7006f5b8)

=> OpbNJ60xYpvAQU8

