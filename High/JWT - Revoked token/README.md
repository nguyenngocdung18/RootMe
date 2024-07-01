![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/40074e6e-e97c-4086-aa70-18ba40242e87)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/79a0b755-9483-429f-befd-7ecd6c4cca09)

Change request method

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/ac74441b-f48c-43af-859b-10a8c28afa14)

Thêm body và thay tôi Content-Type: application/json

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/95753d9f-9409-48f5-a5f2-457b8607c2ec)

=> nhận được token 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/1f67fa07-f60c-408d-b406-3bc98c861706)

Theo source code thì nó sẽ check token ở trong Authorization và xem nó có trong blacklist không. Nếu có thì sẽ loại bỏ, còn không thì
sẽ trả về flag. Các token sau khi được dùng để xác thực sẽ bị đưa vào blacklist

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/95c4e97b-e879-4548-a7a9-b7f8ebac038f)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/14b4f5a7-d24d-40bf-b1cc-17add93068b5)

thêm Bearer

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/714066db-2399-4f3d-a0be-19151db57261)

Vì token jwt được mã hóa bằng Base64 nên ta có thêm thêm dấu = vào cuối để token khác với cái bị đưa vào blacklist nhưng
vẫn giữ được nội dung

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/53e2439c-a11b-4455-a228-00cdaa319374)

=> ```Do_n0t_r3v0ke_3nc0d3dTokenz_Mam3ne-Us3_th3_JTI_f1eld```
