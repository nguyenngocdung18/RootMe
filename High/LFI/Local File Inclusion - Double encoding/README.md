![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/014db9f1-c5e9-4f0b-ae24-188ebbaf4e42)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f071e8ae-a593-4100-babc-ebce080c27a4)

Sau 1 hồi tim kiếm thì có vẻ vector có thể khai thác là php wrapper

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/ffd5c7fd-43ab-4426-af78-66d6b5ad9f09)

Dùng trực tiếp ```php://filter/convert.base64-encode/resource=``` thì tôi thấy không được, nhìn lại đề bài 
là double encoding, tôi encode đoạn mã trên và đã có thể xem được source

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/6b60fa79-08a5-4e60-b1d9-fd09eb67e062)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/37c00860-a2f5-4860-8cbc-10169fa63958)

ta thấy tệp có dùng include("conf.inc.php");. Vì vậy ta thử đọc file conf

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/662c4e72-dedc-46a6-b2d1-c71837839714)


![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/bb327b25-62f0-4cf9-8ebd-d330c8a71fd8)

=> Th1sIsTh3Fl4g!
