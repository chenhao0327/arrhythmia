[TOC]
# arrhythmia
## 准备
- github上生成仓库
- 克隆github仓库到本地
```
 ~   master ●  cd github
 ~/github   master ●  ls
punch_in
 ~/github   master ●  git@github.com:chenhao0327/arrhythmia.git
zsh: no such file or directory: git@github.com:chenhao0327/arrhythmia.git
 ✘  ~/github   master ●  git clone git@github.com:chenhao0327/arrhythmia.git

Cloning into 'arrhythmia'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
 ~/github   master ● 
```
- 布局依赖包
    - `pipreqs --force --use-local ./`
