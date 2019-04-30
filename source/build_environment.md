博客搭建
===========


参考链接: http://python-online.cn/zh_CN/latest/c04/c04_03.html
## 简介
  该博客搭建主要由以下模块及网站实现:
- Sphinx: 生成网页(也可以考虑使用mkdocs)
- reStructuredText: 管理目录结构
- MarkDown: 书写文档
- GitHub: 项目托管
- Pandoc: 格式转换
- ReadTheDoc: 发布网页


## Sphinx搭建

最好使用python2.7, python3似乎不太行, 未深入研究.

安装相关工具包, 所需包均放在 [github项目] 的 requirements.txt

    pip install -r requirements.txt 
在本地文件夹中创建项目目录

    mkdir my_blog
    cd my_blog
初始化项目

    sphinx-quickstart
执行上面命令的时候, 会输入一些基本配置, 除了以下的几个, 其他都可以按默认配置来

    Project name: Rage's Blog
    Author name(s): Rage
    Project release []: 1.0
    Project language [en]: zh_CN
完成配置后, 在项目目录下, 会有生成一些文件, 安装tree, 查看目录结构

    yum install tree
    tree -C .

本地目录结构:
- build: 执行make html, 生成对应的html文件;
- source: 主要的配置文件, 及正文(md或rst文件)存放, 博客目录结构
- Makefile: 编译文件
- make.bat

## 配置及扩展

1.设置Sphinx主题:
  
在 source/conf.py 中添加以下内容:

    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
2.Sphinx支持文件格式设置

Sphinx默认只支持rst格式文件, 习惯使用MarkDown格式, 需在 source/conf.py 中添加以下内容:

    from recommonmark.parser import CommonMarkParser
    source_parsers = {
    '.md': CommonMarkParser,
    }
    source_suffix = ['.rst', '.md']

若不添加此配置, 也可以通过pandoc进行转化

    //安装pandoc
    sudo yum install pandoc
    //将md格式文件转化为rst文件
    pandoc test.md -o test.rst
   
3.一些基本配置, 直接使用 [github项目] 中的 exts 文件移动到项目根目录下, 包含以下配置
- 配置主题
- 支持LaTeX
- 支持中文检索

4.配置 .gitignore 文件

    build/
    .idea/
    *.pyc

## 本地测试
1.新建test.md, 填入以下内容

2.在index.rst以下内容处中添加:

本文档采用rst管理目录结构, md书写文档

其中 `toctree` 为整个目录结构名称及根节点, maxdepth 为当前rst所管理目录结构深度.
之后保留一行空行, 添加当前目录下所具体管理目录内容, 可选择文件夹, 
    
    .. toctree::
        :maxdepth: 3
        :glob:

        preface.rst
        build_environment.md
        Python/Python.rst
         

3.在项目目录下执行make html, 进入build文件夹, 可查看新生成的index.html等.
 

## 发布网站
将创建好的项目上传至github.

在 [ReadTheDocs] 中注册帐号后, 关联自己的github;
找到 `Import a Project`, 选择自己的github项目, 在开始`build`之前, 需对项目做以下设置, 在`管理`下
- 设置>语言
- 高级设置>Python解释器 选择 `CPython 2.x`
- 高级设置>Python配置文件 填写 `source/conf.py`
另外还可设置分支, 语言, 隐私级别等, 看自己需求而定

构建成功后, 找到 `View Docs`, 点击进入项目主页, 查看效果

[github项目]: https://github.com/JustMeliyu/Rage
[ReadTheDocs]: https://readthedocs.org/