# 配置github的登录方法

```shell
# 配置用户名和邮箱地址
git config --global user.name "ligood"
git config --global user.email "lpsh840105.student@sina.com"

# 生成ssh密钥对
ssh-keygen -t rsa -b 4096 -C "lpsh840105.student@sina.com"

# 将内容配置到github的设置页面
cat id_rsa.pub
```
