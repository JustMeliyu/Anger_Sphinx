
# 6.1 Centos7下Mysql安装

1.下载mysql的repo源

    wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
    sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
    
2.安装mysql

    sudo yum install mysql-server

3.修改配置

    sudo chown -R openscanner:openscanner /var/lib/mysql        # 当前用户权限
    systemctl restart mysql     # 重启数据库
    
修改密码, 默认为空

    mysql -uroot -p
    use mysql;
    update user set password=password(‘123456‘) where user=‘root‘;
    exit
    systemctl restart mysql     # 重启数据库

4按utf-8新建数据库

    CREATE DATABASE IF NOT EXISTS my_db default charset utf8 COLLATE utf8_general_ci;
