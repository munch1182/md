# gitcmd

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=4 orderedList=false} -->

<!-- code_chunk_output -->

- [一些命令](#一些命令)
- [设置账号](#设置账号)
- [合并仓库与分支](#合并仓库与分支)
- [创建新的空白分支](#创建新的空白分支)
- [删除远程库的tag](#删除远程库的tag)
- [删除远程库的提交记录](#删除远程库的提交记录)
- [更改提交记录](#更改提交记录)
- [更改分支名](#更改分支名)
- [将一个分支的提交应用到另一个分支](#将一个分支的提交应用到另一个分支)

<!-- /code_chunk_output -->

---

## 一些命令

- 拉取分支到本地    
    `git clone -b [branch] [url]`
- 与远程仓库建立连接(remotename默认origin)  
    `git remote add [remotename] [url]`
- 与远程仓库断开连接    
    `git remote remove origin`
- 查看全部分支  
    `git branch -a`
- 查看远程分支  
    `git branch -r`
- 查看当前状态
    `git status`
- 删除本地分支  
    `git branch -d [branch]`
- 删除远程分支  
    `git push origin --delete [branch]`
- 切换到本地分支并与远程分支连接    
    `git checkout -b [localbranch] orign/[romatebranch]`
- 切换分支  
    `git checkout [branch]`
- 撤销更改到上一次提交(被添加的文件会被删除)  
    `git reset --hard HEAD`
- 撤销更改到指定版本(日志中操作后的一长串即版本号)
    `git reset --hard [versioncode]`
- 查看日志(包括版本号)
    `git log`
- 撤销指定文件的修改    
    `git chceckout HEAD [file]`
- 列出所有tag   
    `git tag`
- 基于最新提交创建标签  
    `git tag [tag]`
- 删除指定标签  
    `git tag -d [tag]`
- 推送所有tag   
    `git push --tags`
- 提交  
    `git commit -a -m "[message]"`
- 拉取无关库代码，即两个库合并  
    `git pull origin master --allow-unrelated-histories`

## 设置账号

- 设置全局账户  
    `git config --global user.name "[username]"`    
    `git config --global user.email "[useremail]"`
- 单个项目去掉--global，也可直接修改.git/config文件，加入 
    ```
    [user]
        name = you name
        email = youemail@host.com
    ```
- 清理账号  
    `git config --global --unset user.name`     
    `git config --global --unset user.email`

## 合并仓库与分支

- 通过建立多个以远程名区分的远程地址，拉取一个远程的分支，并推送到另一个远程的分支
- 进入最终的仓库
- 与需要合并的远程仓库建立连接，需要不同的remotename
    - 查看远程名：`git remote`
    - `git remote add [remotename] [url]`
- 拉取代码
    - `git pull [remotename]`
- 切换到需要合并的远程仓库分支
    - 查看所有分支：`git branch -a`
    - 查看远程分支：`git branch -r`
    - `git checkout -b [branch] [remotename]/[branch]`
- 推送到最后的仓库
    - `git push origin [branch]`

- 同理，将当前代码推送到另一个代码仓库，需要将该远程地址添加并拉取该仓库，然后推送到该仓库和相应的分支即可

## 创建新的空白分支 

- 创建一个不带提交记录的分支    
    `git checkout --orphan [branch]`
- 删除分支带出的文件    
    `git rm -rf .`
- 空提交来生成分支  
    `git commit --allow-empty -m "[commit]"`
- 推送到远程    
    `git push origin [branch]`

## 删除远程库的tag 

- 删除tag   
    `git tag -d [tag]`
- 推送到远程库 
    `git push origin :[tag]`

## 删除远程库的提交记录

- 本地回退到相应版本，使用`--hard`替换`--soft`则不会保留自相应版本以来的更改记录    
    `git reset --soft [versioncode]`
- 推送到远程库，并使用`--force`     
    `git push --force`

## 更改提交记录

- 执行以下命令，3为最近三次
    `git rebase -i HEAD~3`
- 将要修改的相应记录前的`pick`更改为`edit`，然后使用`:wq`退出编辑器
- 执行命令并修改记录，使用`:wq`保存退出
    `git commit --amend`
- 完成修改
    `git rebase --continue`
- 强制推送到远程
    `git push -f`

- 如果只修改最近一次的记录，可以直接从第三步开始
- 如果修改错误，可以直接删除`.git/rebase-merge`文件夹重新开始
- 文件编辑方法参照linux的文本编辑器
- 可以使用`git log`查看日志

## 更改分支名 

- 本地更改：   
    `git branch -m [oldbranch] [newbranch]`
- 更改远程：    
    - 删除远程分支  
        `git push --delete origin [branch]`
    - 上传本地分支  
        `git push origin [branch]`
    - 关联本地分支与远程分支    
        `git branch --set-upstream-to origin/[branch]`

## 将一个分支的提交应用到另一个分支

- 切换到代码更改的分支，查看提交的hash值
    `git log -4` //查看最近4次提交
- 切换到需要被应用的分支，合并提交
    `git cherry-pick [hash]`或者`git cherry-pick [hash]..[hash]`//hash只需要前7位

- 需要注意冲突的解决