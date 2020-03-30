# **USTCBBhelper**-USTC中科大BB系统更新助手

方便你快速更新BB系统中的课程资源

可自动分成多个文件夹,不覆盖已有文件

## 如何使用:

### step1:

安装有pyhton3和pip3,并安装一下依赖

pip install Beautifulsoup4

pip install requests

### step2:

配置config.py

替换data中的username和password为自己的ustc学号和密码

替换des为你想要的保存路径

### step3:

python bbhelper.py

然后你的BB课程资源会按课程,按网页上的分类,整理好后放在des目录下

## 现有的问题:

文件的不覆盖验证在get到文件之后,增量更新很慢(待解决)

不能抓取视频页面,暂时用ban_list的设置来不爬取一些资源,如以下页面:

![image-20200330150124487](https://github.com/gy991007/USTCBBhelper/blob/master/issue1.png)

