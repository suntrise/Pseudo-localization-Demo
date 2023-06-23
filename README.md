# 伪本地化演示程序

![截图](https://github.com/suntrise/Pseudo-localization-Demo/assets/89229642/51b8023e-ebb6-4c74-b3f1-b41fbdfd6c5b)

这是一个伪本地化工具，可用于某些本地化工作用途，当然也可以作为一个玩具或者工具

网页版：https://suntrise.github.io/pseudo

## 使用

注意，要在本地查看并修改源码，需要安装Python，版本最少为3.7以保障兼容性

### Windows

若要编辑使用，请先运行`1.install repuirement.bat`安装依赖

若要编译，安装完依赖后直接运行`2.build into binary.bat`即可

### 其它系统

#### 编辑&使用

运行...

~~~Bash
pip install flet
pip install pyperclip
~~~

安装依赖，若需编辑旧版，则还需要额外运行......

~~~Bash
pip install PyQt5 
~~~

原则上`PyQt6`也行，各位可以试试

#### 编译

运行......

~~~Bash
pip install pyinstaller
~~~

定位到代码根目录，运行......

~~~Bash
pyinstaller pslo.pyw -F -w -i pslo_icon.ico
~~~

编译完可能需要Wine或者Crossover才可以运行，因此我们依旧推荐直接执行pyw文件

## 使用到的第三方项目

### 2.x

[flet-dev/flet](https://github.com/flet-dev/flet)

[makinacorpus/django-paperclip](https://github.com/makinacorpus/django-paperclip)

### 1.x

[Riverbank Computing PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
