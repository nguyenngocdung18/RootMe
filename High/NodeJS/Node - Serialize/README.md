 ![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/82dc2477-a1e7-46de-a40b-c883ea17ff98)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/206a082e-baf8-426b-b718-191b0746f7a3)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/7a3aabd5-884e-4398-a942-abce9b0ddc3f)

decode cookie 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/72d2ec7a-c758-4d0e-91ce-80a65cd4c0b2)

Trên Hacktrick, ta tìm thấy đoạn code serialize bằng nodejs

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/8e5b3f7a-7355-47ff-8c1a-1359172d00d6)

tạo 1 file .js để tiến hành RCE

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/1e484875-3e3b-46ee-98cf-4a0b584ef5df)

Dùng module node-serialize, ta có 1 chuỗi như dưới đây

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/6fc95db3-3a93-4336-8590-c40fd5c04ca7)

Giờ ta chỉ cần encode lại và copy vào phần cookie nữa là hoàn thành

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c4cc70f3-06ab-438d-a0ba-67a7b1c23e73)

=> flag: Y3pS3r0d3c0mp4nY1sB4d!
