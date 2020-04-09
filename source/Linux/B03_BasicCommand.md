# 2.3 常用Linux命令

## find
从 '/' 开始进入根文件系统搜索文件和目录, 可模糊查询

    find / -name file1 
从当前目录及子目录获取最近20天有更新的文件

    find . -ctime -20 
- `atime` 过去几天内被读取过的文件
- `amin` 过去 n 分钟内被读取过的文件
- `ctime` 过去几天被修改过的文件
- `cmin` 过去几分钟被修改过的文件

## awk

awk 是一个文本处理的应用程序, 它会依次处理文件的每一行, 并读取里面的每一个字段, 
适合处理标准日志及CSV格式等文件, 这里介绍其简单的应用;

1.语法格式

    awk 动作 文件
    awk '{print $0}' test.log
    
通过单引号包含动作, `print` 为打印文本, `$0` 代表当前行;

2.awk 也可以通过指定字符(默认为空格), 按每一行进行分割, 并获取分割后指定的第几个字符. 具体如下:

- `-F` 指定分割符, 
- `$1`, `$2`, `$3`... 获取分割后的第一, 二, 三个字符. 
- `$NF`, `$(NF-1)` 依次代表最后一个, 倒数第二个
- `NR`, 代表当前处理第几行
- 另外还提供一些函数, 条件, if语句等, 具体见 **[参考](http://www.ruanyifeng.com/blog/2018/11/awk.html)**

test.log:
    
    2019-05-04 17:12:32|ERROR|recoding_oa|23595|system|recoding_oa||success||flowid 16a56ba3a5bba6525f3eb774d539cb61 is not exist|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||current flow id is 16a56ba28ad1792892a27414939a6dec|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||<type 'datetime.datetime'>|
    2019-05-04 17:12:32|ERROR|recoding_oa|23595|system|recoding_oa||success||flowid 16a56ba28ad1792892a27414939a6dec is not exist|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||current flow id is 16a56ba3a4b0d5d00d887404c22b8518|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||<type 'datetime.datetime'>|
    2019-05-04 17:12:32|ERROR|recoding_oa|23595|system|recoding_oa||success||flowid 16a56ba3a4b0d5d00d887404c22b8518 is not exist|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||current flow id is 16a56ba2f675404246cf48944c8ada06|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||<type 'str'>|
    2019-05-04 17:12:32|INFO|recoding_oa|23595|system|recoding_oa||success||16a56ba2f675404246cf48944c8ada06 is not finish, PASS|
        
使用 `awk -F "|" '{print NR ") " $2, $(NF-1)}' test.log`, 效果如下:

    20600) ERROR flowid 16a56ba3a5bba6525f3eb774d539cb61 is not exist
    20601) INFO current flow id is 16a56ba28ad1792892a27414939a6dec
    20602) INFO <type 'datetime.datetime'>
    20603) ERROR flowid 16a56ba28ad1792892a27414939a6dec is not exist
    20604) INFO current flow id is 16a56ba3a4b0d5d00d887404c22b8518
    20605) INFO <type 'datetime.datetime'>
    20606) ERROR flowid 16a56ba3a4b0d5d00d887404c22b8518 is not exist
    20607) INFO current flow id is 16a56ba2f675404246cf48944c8ada06
    20608) INFO <type 'str'>
    20609) INFO 16a56ba2f675404246cf48944c8ada06 is not finish, PASS

## history
`history` 查看历史执行命令

1.一些配置：
- 配置文件在 `/etc/profile` 中;
- `HISTSIZE` 设置记录行数;
- 在`/etc/profile` 中添加`export HISTTIMEFORMAT="%y-%m-%d %H:%M:%S "` 可设置显示时间
 
2.`history [n]` 查看最近n条记录

## ps


## netstat
Netstat 命令用于显示各种网络相关信息，如网络连接，路由表，接口状态 (Interface Statistics)，masquerade 连接，多播成员 (Multicast Memberships) 等等

参数如下:
    
    -a (all)显示所有选项，netstat默认不显示LISTEN相关
    -n 拒绝显示别名，能显示数字的全部转化成数字。(重要)
    -l 仅列出有在 Listen (监听) 的服務状态
    -s 按各个协议进行统计 (重要)
    -p 显示建立相关链接的程序名(macOS中表示协议 -p protocol)
    
    -t (tcp)仅显示tcp相关选项
    -u (udp)仅显示udp相关选项
    -r 显示路由信息，路由表
    -e 显示扩展信息，例如uid等
    -c 每隔一个固定时间，执行该netstat命令。
 
 
查看端口占有情况

    netstat -lnp |grep 5001
    
## 软链接与硬链接

软链接是一个快捷方式，当源文件没有时，就找不到，只能使用绝对路径
硬链接是一个别名，多个别名代表同一个文件，当删除一个文件时，依旧可以找到之前的。可以使用相对地址

## more与less区别

- more 不可后退，less 可以后退
- less可以通过方向键上下键显示内容，more不可以
- less不必读整个文件，加载速度比more更快
- less退出不会显示刚才查看的内容，而more会
