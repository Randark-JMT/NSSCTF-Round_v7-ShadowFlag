# NSSCTF Round$7 ShadowFlag

都rm -f执行过了，flag还能找到吗

## 题目考点
- `/proc/<pid>/fd`文件系统
- 新版本Flask Debug PIN计算
- Flask Debug界面调取变量数据
  
## 解题流程
请参阅项目目录:`./document/poc.py`
在脚本中，备注部分给出了一份无空格Python反弹shell的指令(注意修改为自己的监听地址)，并且此脚本为高版本Flask计算Debug PIN的脚本。步骤如下:
1. 访问靶机，可以看到`app.py`源码，其中可以看到整体的路由和逻辑
2. 访问`ip:port/shell`，用过`POST`方法发送上文的无空格反弹shell，即可得到shell
3. 参考赵总的这篇文章[2020 年 V&N 内部考核赛 WriteUp - Glzjin](https://www.zhaoj.in/read-6407.html)，访问到前半部分flag
4. 阅读`poc.py`中的注释说明，通过shell读取到相应的环境数据，计算出Debug PIN
5. 访问`ip:port/shell`，用过`POST`方式，随便POST数据(只要不包含`act`这个变量)，或者直接访问`ip:port/console`，即可触发错误，进而进入Flask Debug界面
6. 利用上文计算得到的Debug PIN，进入Debug控制台，执行`flag2`或者`dump()`，即可读取到变量数据，进而得到flag2
7. 两段flag拼接，即可解出

## 环境部署
项目已给出`Dockerfile`，直接执行`docker build`即可构建镜像
本项目支持动态flag($FLAG传入)，部署容器可使用CTFd，或参考`./docker/docker-compose.yml`