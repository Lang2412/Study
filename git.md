# github 入门
## 1.git安装
windows 安装地址:https://gitforwindows.org/
## 2.使用前期准备
* 设置姓名和邮箱地址

    `$ git config --global user.name "name"`<br>
    `$ git config --global user.email "your_email@example.com"`
    
    可以使用`cat ~/.gitconfig`命令查看设置的内容，也可以直接编辑`./gitconfig`文件修改内容。
    
* 提高命令输出的可读性

    `$ git config --global color.ui auto`
    
    `.gitconfig`文件中会增加下面一行，使得各种输出颜色有区别，增加可读性。
    
    `[color]`<br>
    `  ui = auuto`
    
* 创建github账户并设置SSH Key

    1.登录 https://github.com 创建账户
    
    2.设置SSH Key
    
      `$ ssh-keygen -t rsa -C "your_email@example.com"`
      
      此过程会让你再次输入两次密码，最后生成两个文件`id_rsa`和id_rsa.pub`,其中`id_rsa`是私有秘钥，`id_rsa.pub`是公开秘钥。
      
      进入github中，右上角找到Account Settings,选择SSH Ker菜单，点击 Add SSH Key进行设置，Title输入想要的秘钥名称，Key部分
      粘贴`id_rsa.pub`文件中的内容。
      
      `$ cat ~/.ssh/id_rsa.pub`
      
      设置成功后github账户绑定邮箱会收到一封邮件，此时可以用私有秘钥与github进行通信了。输入以下代码
      
      `Enter passphrase for key '/c/Users/疯狼/.ssh/id_rsa':
      `Enter passphrase for key '/c/Users/疯狼/.ssh/id_rsa':
      `Hi Lang2412! You've successfully authenticated, but GitHub does not provide shell access.
      
      成功！
      
## 常用命令
       
    git branch                  查看本地所有分支
    git branch -r               查看远程所有分支
    
    git status                  查看当前状态
    
    git commit                  提交
    git commit -am "init"       提交并加注释信息"init"
    git commit --amend          修改提交信息，进入编辑器进行修改
    
    git add  文件名              将文件放入暂存区
    
    git log                     查看提交日志
    git log --graph             以图形方式查看提交日志
    git reflog                  查看当前仓库执行过的操作的日志
    
    git push                    push一下，github上的仓库就更新了
    
    git init                    初始化
    
    git diff                    查看当前工作树与暂存区的差别
    git diff HEAD               查看当前工作树与上次提交的区别
    
    git checkout -b A           创建新的本地分支A
    git checkout A              切换到本地A分支
    git checkout -              切换到上一个分支
    
    git merge --no-ff A         将当前分支与A分支合并，并留下历史记录信息
    
    git reset --hard            回溯历史版本，需要在后面提供想要回溯的状态的哈希值，可以通过 git reflog 指令查看每一个提操作的日志和哈希值
    
    git branch -D master A      删除本地库A      
    
    git remote add origin https://github.com/用户名/仓库名      设置本地仓库的远程仓库
    git push -u origin master                                   将文件推送到服务器上
    
    git clone https://github.com/count/hellow.git               从服务器将仓库克隆到本地
    
    git pull                    本地与服务器端同步

      
      
    
    
  
  
  
 
