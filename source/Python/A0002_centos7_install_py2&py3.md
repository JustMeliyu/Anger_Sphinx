**无财作为, 少有斗智, 既饶争时**

1.2 centos7下py2与py3的共存
===========================

## 依赖环境

    yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

## 安装python3
获取python3
    
    wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
    //解压
    tar -zxf Python-3.7.2.tgz
    cd Python-3.7.2

配置编译安装
建议添加 --prefix，安装到指定目录

    ./configure --prefix=/usr/local/python3
    make &&make install

## 配置

1.为python3添加软链接

    ln -s /usr/local/python3.7/bin/python3.7 /usr/bin/python3
 
2.如果想将python3设置为默认，也可以

    ln -s /usr/local/python3.7/bin/python3.7 /usr/bin/python

python2还存在 python2命令
不过由于centos7 `yum` 命令依赖python2，所以需对以下文件的头部作修改
及将 `/usr/bin/python` 修改为 `/usr/bin/python2`

    vim /usr/bin/yum
    vim /usr/libexec/urlgrabber-ext-down
    vim /usr/bin/yum-config-manager

## 安装pip3

1.获取安装包

    wget https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
    tar -zxvf setuptools-19.6.tar.gz 
    cd setuptools-19.6
    python3 setup.py build 
    python3 setup.py install

这里的"python" 取决于之前安装python3时定义的 python3或python
 
2.添加软链接

    ln -s /usr/local/python3.7/bin/pip3 /usr/bin/pip3

若也想将pip3默认为pip，也可以

    ln -s /usr/local/python3.7/bin/pip3 /usr/bin/pip

python2的pip此时可以使用pip2继续使用
