![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/5b803f0b-f635-4b2b-a8e5-94f3dbd1ba33)

click vào English => trên URL xuất hiện lang=en

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/e26cb34c-a976-4963-b5fe-7feef5e5b9b6)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c1cfa0cb-08a9-4448-adec-fc0783944103)

ta thấy 2 dòng
```
include(index.php_lang.php)
include_path:/usr/share/php
```
tôi tạo 1 gist

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/68361e6c-2797-4538-8907-df6a1def8485)

chọn raw để hiện tên file trong URL

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/46b8060b-b5c5-4e30-8874-b5ad99016b81)

Giờ chỉ cần copy URL của gist này bỏ đi "_lang.php" và tadaa~~~

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a15daeb3-703a-4579-ae22-136ce2cdb1fa)

=> R3m0t3_iS_r3aL1y_3v1l

À thì tôi có đi tìm hiểu thêm thì bài này làm được vậy do nó bật allow_url_include, 
chứ nếu không thì không cách nào chèn URL vào đâu =)))

