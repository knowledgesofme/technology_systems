
# 关键设置

```shell
# https://opsx.alibaba.com/mirror
deb https://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse 
deb https://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse 
deb https://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse 
deb https://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse 
deb https://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse 

# 仿照清华镜像源，注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
# deb-src https://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse 
# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse 
# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse 
# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse 
# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse


sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
apt-get install gdb


uname lily,root
passwd 120503
```