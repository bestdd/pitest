> 这是一个让你快速入手、快速入门的自动化工具 
```
pitest 是一个快速简单搭建的接口自动化工具

使用技术：unitest paramunitest requests  htmltestrunner mysql 
测试入口方法：core/test.py

追寻能力的过程是价值的实现
```
### 使用步骤
- 安装工具：python3+下载安装配置（百度即可）
- 安装工具：pycharm/其他python编译器 下载安装、导入项目 （百度即可）
- 安装依赖包： pip install -r requirements.txt
- 配置需要测试校验数据库
```
请配置需要校验的数据库，如果没有可使用示例sql文件，学习效果 
[1]新建数据库，导入pitest/resource/itest.sql
[2]修改数据库配置文件 pitest/common/mysql_utils.py
```
- 启动需要测试的项目
```
用做接口测试（推荐使用自己的项目调试入门）
[1]cd pitest/resource//resources
[2]java -java itestAPI-1.0.jar 
```
- 录入用例：pitest/resource/case-template.xlsx
- 启动测试：py test.py
- 测试报告：report/report.html

![](https://ae01.alicdn.com/kf/Heedc57be6d904e52921a707ce5719816r.png)
### 帮你学习
使用技术：unitest paramunitest requests  htmltestrunner mysql   
在demo包、common包中，有简单示例代码，参考使用即可

##可能遇到的问题

1.修改pip国内源
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  
参考：https://blog.csdn.net/liushimiao0104/article/details/96475364

2.关于HTMLTestRunner无法生成报告
右击运行，可能存在unittest加载的问题。
正确方式为 Alt+shift+F10，选择不带Unittests的那条执行，就是直接选择该python文件名执行

