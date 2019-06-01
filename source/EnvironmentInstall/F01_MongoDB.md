
# 6.1 Centos7下MongoDB及GUI安装

### MongoDB安装

1.添加源

切换到源目录， 并创建文件
    
    cd /etc/yum.repos.d/
    touch mongodb-3.4.repo
    
添加一下内容

    [mongodb-org-3.4]
    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
    gpgcheck=0
    enabled=1
    gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc
       
2.安装

源安装

    yum  install -y mongodb-org
    
启动MongoDB, 默认未启动

    systemctl start mongod.service

3.配置

查看配置文件 `/etc/mongod.conf`, 主要`bindIP`以及`port`, 默认如下

    port: 27017
    bindIp: 127.0.0.1
    
创建超级权限用户

    use admin
    db.createUser({user:'root',pwd:'root',roles:[{ "role" : "root", "db" : "admin" }]});

    
### GUI工具, adminMongo

1 源码

    git clone https://github.com/mrvautin/adminMongo
    
2.安装

    yum install nodejs      # npm安装
    npm install             # 安装
    npm start               # 启动
    
3.访问

    http://127.0.0.1:1234
    
Connection name, 随便填
Connection string, mongodb://127.0.0.1    
