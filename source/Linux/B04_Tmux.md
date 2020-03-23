**无财作为, 少有斗智, 既饶争时**

2.4 虚拟终端---tmux
============

## 2.4.1 简介

tmux: Terminal MultipleXer,意思是终端复用器;

主要可在一个窗口操作多个会话, 主要三个概念: 会话(session), 窗口(window)以及窗格(pane), 我们实际操作的单位是pane


## 2.4.2 修改配置

由于tmux默认操作快捷键是ctrl + b, 使用补台方便, 所以可以修改默认快捷键为 ctrl + a, 配置如下:

    set -g prefix C-a                                                                           │[ly@localhost ~]$ 
    unbind C-b                                                                                  │[ly@localhost ~]$ 
    bind C-a send-prefix
    
## 2.4.3 会话

由终端进入tmux会话
### 1. 创建一个新会话

    tmux new -s session_name
  
`-s` 是指session, 创建后会由终端进入会话中, 如下图所示

底部绿色区域, 依次显示会话名, 当前会话的窗口序号, 窗口名称

### 2.会话常用命令

`ctrl+a d`  退出tmux会话

`tmux ls` 展示所有tmux会话

`tmux a -t session_name` 进入指定session_name会话, `a` 代表 attach, -t 表示进入已存在的会话

`ctrl+a s` 在会话中展示所有会话, 其中 attached 表示该会话是当前会话

`tmux kill-session -t session_name`, 销毁会话(在终端环境); 在会话环境中 `ctrl+a :`, 再输入 `kill-session -t session_name`, 同样可销毁会话

`tmux rename -t old_session_name  new_session_name` 重命名会话(在终端环境)

`ctrl+a $` 重命名会话(在会话环境)

## 2.4.4 窗口(window)

每个会话可以有多个窗口

### 窗口常用命令

`ctrl+a c` 创建一个新窗口; 创建一个新窗口后, 在底部绿色区域会新增一个窗口信息; 序号依次添加, 带 `*` 为当前窗口

`ctrl+a p` (previous的首字母) 切换到上一个window。

`ctrl+a n` (next的首字母) 切换到下一个window。

`ctrl+a 0` 切换到0号window,依次类推,可换成任意窗口序号

`ctrl+a w` (windows的首字母) 列出当前session所有window,通过上、下键切换窗口

`ctrl+a l` (字母L的小写)相邻的window切换

`ctrl+a &` 关闭当前窗口

`ctrl+a ,` 重命名当前窗口


## 2.4.5 窗格(pane)

pane 才是真正意义上操作的最小单位

### 窗口常用命令

`ctrl+a %` 可以将窗口垂直分屏

`ctrl+a :` 可以将窗口水平分屏

分屏后, 光标停留在哪个pane, 表示pane是活动, 绿色框表示当前活动pane

`ctrl+a o` 依次切换当前窗口下的各个pane

`ctrl+a Up|Down|Left|Right` 根据按箭方向选择切换到某个pane.

`ctrl+a Space (空格键)` 对当前窗口下的所有pane重新排列布局, 每按一次, 换一种样式.

`ctrl+a z` 最大化当前pane, 再按一次后恢复

`ctrl+a x` 关闭当前使用中的pane, 操作之后会给出是否关闭的提示, 按y确认即关闭.

## 2.4.6 查看历史输出

在tmux里面,因为每个窗口(tmux window)的历史内容已经被tmux接管了, 
当我们在每个tmux的window之间进行来回切换, 
来回操作,那么我们没有办法看到一个window里面屏幕上的历史输出. 
没办法使用鼠标滚动(例如在SecureCRT中)查看之前的内容, 
在SecureCRT中通过鼠标滚动看到的输出一定是各个tmux的window的输出混乱夹杂在一起的, 
如果要看当前窗口的历史内容, 那么应该怎么办呢. 
通过在当前的tmux window 按 ctrl-b 进入copy mode, 
然后就可以用PgUp/PgDn来浏览历史输出了, 按q退出.