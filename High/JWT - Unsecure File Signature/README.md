![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/9da0785c-ef2e-4319-86b3-85507060b78e)

:v click vào nút html-lecture nhưng có vẻ đây không phải flag cần tìm

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/4df64bf0-3c32-454e-9bd4-619913ae9565)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/d5ed49d8-72a5-4769-b798-8f60d2c8b7d0)

Decode 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f24402ae-593b-40f5-a5f9-51517e784ec7)

Ta thấy 1 thuộc tính mới trong phần header "kid"

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/21c41ce5-b6b4-42d9-86d5-54e94c03d203)

=> Không phải admin

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/8f70fbb9-3d88-4ad4-88e5-24870128069d)

Đổi guest -> admin thì không được

Thử đổi thuộc tính kid

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/db597cd8-f59b-48f8-af4e-b1eccecc7086)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/f91408e5-8bbb-49e6-bbd9-e20ee2317a0a)

có một thông báo là "File keys/a not found"

Thử với 1 vài input khác

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/222c82e7-845f-4851-ae7e-17d4a67e590e)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/1e2344de-2385-4de5-acd3-a114b97275e2)

Có vẻ như ../ đã được replace

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/7fd3a7d9-b90a-4530-850f-c87c13aea134)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a6ef359b-1a89-4dda-bf20-62acae9d5d9b)

quả thật là như vậy. Từ đây ta có thể đoán là nó sẽ tìm tới file trong giá trị của kid để check author

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/9391ef9c-175e-417f-998a-13075759a188)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/cb3ebf5d-8d5b-418d-9081-3c0d6fff8ca9)

=> RM{Uns3cUr3_f1l3_H4ndl1nG!!}
