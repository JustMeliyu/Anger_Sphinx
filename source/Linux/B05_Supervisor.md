**无财作为, 少有斗智, 既饶争时**

2.5 进程管理程序---supervisor
============================

### 2.5.1 安装

1.yum安装

    yum install supervisor
    
2.pip安装

    pip install supervisor
    
### 2.5.2配置

1.设置配置文件目录

    mkdir /etc/supervisor
    
2.初始化配置文件

    echo_supervisord_conf > /etc/supervisor/supervisord.conf
    
3.添加子进程配置文件

首先在配置文件目录添加一个存放子进程配置文件的目录: conf.d; 
然后在supervisord.conf的文件尾部, 添加如下配置

    [include]
    files = /etc/supervisor/conf.d/*.conf
    
这里的作用是为将各个子进程的配置文件包含进来

4.子进程配置文件
    
    #项目名
    [program:platform_celery]
    #脚本目录
    directory = /home/ly/code/camel_project/intelligent_park/backend/celery_platform
    #脚本执行命令
    command = /usr/bin/python2 /bin/celery -A platform_srv worker -c 2 -l info
    
    #supervisor启动的时候是否随着同时启动，默认True
    autostart = true
    
    #这个选项是子进程启动多少秒之后，此时状态如果是running，则我们认为启动成功了。默认值为1
    startsecs=5
    
    #当程序exit的时候，这个program不会自动重启,默认unexpected，设置子进程挂掉后自动重启的情况，
    #有三个选项，false,unexpected和true。如果为false的时候，无论什么情况下，都不会被重新启动，
    #如果为unexpected，只有当进程的退出码不在下面的exitcodes里
    autorestart = true
    
    
    #脚本运行的用户身份 
    user=root
    
    #把stderr重定向到stdout，默认 false
    redirect_stderr = true
    
    #stdout日志文件大小，默认 50MB
    stdout_logfile_maxbytes = 50MB
    
    #stdout日志文件备份数
    stdout_logfile_backups = 20
    
    #日志输出 
    stdout_logfile = /home/ly/code/camel_project/logs/platform.log
    

### 2.5.3 supervisor 启动

1.开机启动

新建一个 `supervisord.service` 文件

    # dservice for systemd (CentOS 7.0+)
    # by ET-CS (https://github.com/ET-CS)
    [Unit]
    Description=Supervisor daemon
    
    [Service]
    Type=forking
    ExecStart=/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
    ExecStop=/usr/bin/supervisorctl shutdown
    ExecReload=/usr/bin/supervisorctl reload
    KillMode=process
    Restart=on-failure
    RestartSec=42s
    
    [Install]
    WantedBy=multi-user.target

存放至 `/usr/lib/systemd/system/` 目录下; 执行命令
    
    systemctl enable supervisord 

2.启动服务

    systemctl start supervisord
    
或者

    supervisord -c /etc/supervisor/supervisord.conf

如果启动失败, 可能是已经被启动, 可杀死相关进程, 重新启动


### 2.5.4 常用命令

    supervisorctl restart <application name> ;重启指定应用
    supervisorctl stop <application name> ;停止指定应用
    supervisorctl start <application name> ;启动指定应用
    supervisorctl restart all ;重启所有应用
    supervisorctl stop all ;停止所有应用
    supervisorctl start all ;启动所有应用

