**无财作为, 少有斗智, 既饶争时**

3.2 redis
==========

## 3.2.1 redis 持久化

持久化的两种方式
- RDB: 每隔一段时间就对Redis里面的数据做一次快照
- AOF: 记录每次服务器写的操作，重启服务器时，会重新执行这些命令来恢复原始数据

## 3.2.2 redis 在Mac上设置开机自启动

[配置文件](../_static/DataBase/com.redis.plist)

[参考链接](https://www.jianshu.com/p/4addd9b455f2)