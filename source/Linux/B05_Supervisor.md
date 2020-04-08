**无财作为, 少有斗智, 既饶争时**

2.5 进程管理程序---supervisor
============================

## 2.5.1 安装

1.yum安装

    yum install supervisor
    
2.pip安装

    pip install supervisor
    
## 2.5.2配置

1.设置配置文件目录

    mkdir /etc/supervisor
    
2.初始化配置文件

    echo_supervisord_conf > /etc/supervisor/supervisord.conf
    
在这个配置文件中，有几个重要的配置

`supervisorctl` 是`supervisor`的客户端，它实现命令行来使用`supervisord`服务端功能，通过`supervisorctl`，
可以连接到`supervisord`服务器进程，进而获得服务器进程的子进程状态，启动和停止子进程，获得正在运行的进程列表。
客户端通过`Unix域套接字`或者`TCP套接字`与服务端进行通信，服务器端具有身份凭证认证机制，可以有效提升安全性。
当客户端和服务器位于同一台机器上时，客户端与服务器共用同一个配置文件/etc/supervisord.conf，通过不同标签来区分两者的配置。

    [unix_http_server]
    file=/tmp/supervisor.sock   ;UNIX socket 文件，supervisorctl 会使用
    ;chmod=0700                 ;socket文件的mode，默认是0700
    ;chown=nobody:nogroup       ;socket文件的owner，格式：uid:gid
    
    ;[inet_http_server]         ;HTTP服务器，提供web管理界面
    ;port=127.0.0.1:9001        ;Web管理后台运行的IP和端口，如果开放到公网，需要注意安全性
    ;username=user              ;登录管理后台的用户名
    ;password=123               ;登录管理后台的密码
     
    [supervisord]
    logfile=/tmp/supervisord.log ;日志文件，默认是 $CWD/supervisord.log
    logfile_maxbytes=50MB        ;日志文件大小，超出会rotate，默认 50MB，如果设成0，表示不限制大小
    logfile_backups=10           ;日志文件保留备份数量默认10，设为0表示不备份
    loglevel=info                ;日志级别，默认info，其它: debug,warn,trace
    pidfile=/tmp/supervisord.pid ;pid 文件
    nodaemon=false               ;是否在前台启动，默认是false，即以 daemon 的方式启动
    minfds=1024                  ;可以打开的文件描述符的最小值，默认 1024
    minprocs=200                 ;可以打开的进程数的最小值，默认 200
     
    [supervisorctl]
    serverurl=unix:///tmp/supervisor.sock ;通过UNIX socket连接supervisord，路径与unix_http_server部分的file一致
    ;serverurl=http://127.0.0.1:9001 ; 通过HTTP的方式连接supervisord


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
    

## 2.5.3 supervisor 启动

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


## 2.5.4 常用命令

    supervisorctl restart <application name> ;重启指定应用
    supervisorctl stop <application name> ;停止指定应用
    supervisorctl start <application name> ;启动指定应用
    supervisorctl restart all ;重启所有应用
    supervisorctl stop all ;停止所有应用
    supervisorctl start all ;启动所有应用

