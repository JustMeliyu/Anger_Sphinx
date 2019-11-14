**无财作为, 少有斗智, 既饶争时**

2.99 其他---Other
====================

### 2.99.1 vim一些习惯设置

修改配置文件`/etc/vimrc`
1.设置tab默认4个空格，以及自动换行；

    set ts=4
    set expandtab
    set autoindent
    
2.显示行号

    set number
    
3.打开语法高亮

    syntax on
    
4.按下 `>>` (两个大于符号)增加一级缩进; 按下 `<<` (两个小于符号)减少一级缩进

    set expandtab
    
5.光标所在行高亮

    set cursorline
    
6.光标移到到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号

    set showmatch
    
7.打开英语单词的拼写检查

    set spell spelllang=en_us


具体配置文件 [vimrc](../Linux/vimrc)
