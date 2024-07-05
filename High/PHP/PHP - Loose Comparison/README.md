![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/5f5d7839-ced6-4a1e-ba9f-0f2e24f7efd7)

Ấn vào source code

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/dcd9b68a-5856-4280-a68f-e6f1ea1523be)

+ Người dùng nhập s và h vào form.
+ s được làm sạch và h được hash bằng MD5.
+ Một số ngẫu nhiên r được tạo ra.
+ Ghép chuỗi s và r, kiểm tra nếu bằng hash của h.

=> Nếu đúng, in ra flag, nếu sai, in ra thông báo lỗi

Dựa vào source, ta có thể đoán được kiểu dữ liệu trả về của từng biến
```
$s => trả về String
$h => trả về String
$r => int
$s.$r => String
```
Và vì bài này sử dụng so sánh lỏng lẻo (Loose Comparison). 
Chuỗi 0e123456789 có định dạng giống như một số khoa học (scientific notation).

Ví dụ:
+ 0e123456789 có nghĩa là 0 nhân với 10^123456789
+ 0e987654321 có nghĩa là 0 nhân với 10^987654321.
+ Bởi vì bất kỳ số nào nhân với 0 đều bằng 0, cả hai chuỗi này sẽ được PHP chuyển đổi thành số 0 trước khi thực hiện so sánh.

Nên ta sẽ đi tìm mã Hash bắt đầu bằng 0e và đằng sau toàn là số thì khi thêm $r nó vẫn sẽ trả về True!!! Ta tìm thấy payload sau:
```
$s=0e830400451993494058024219903391
$h=QNKCDZO
```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/2a162763-8339-453b-acb1-93ffc777f4c3)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/6dee7bbf-032b-4fbd-91eb-31c9bd319cfd)

=> F34R_Th3_L0o5e_C0mP4r15On
