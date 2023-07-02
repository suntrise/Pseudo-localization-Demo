# 🌐伪本地化演示程序

![image](https://github.com/suntrise/Pseudo-localization-Demo/assets/89229642/d0096413-c0a7-4e8f-8d63-1fe7050badb2)
![image](https://github.com/suntrise/Pseudo-localization-Demo/assets/89229642/c19f2f18-368a-41ed-b40e-5059ea0f414e)

这是一个伪本地化工具, 可用于某些本地化工作用途, 当然也可以作为一个玩具或者工具~

网页版：https://suntrise.github.io/pseudo

## 👇使用

注意, 要在本地查看并修改源码, 需要安装Python, 版本最少为3.7以保障兼容性

### 🚀依赖安装

运行...

~~~Bash
pip install flet
pip install pyperclip
~~~

安装依赖, 若需编辑旧版, 则还需要额外运行......

~~~Bash
pip install PyQt5 
~~~

使用`PyQt6`稍加修改其实也行, 不过组件可能会变大

如果嫌慢可以改用清华源, 参考[此处](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

### 🛠️编译

#### Pyinstaller (简单)

运行......

~~~Bash
pip install pywin32
pip install pyinstaller
~~~

定位到代码根目录, 运行......

~~~Bash
pyinstaller pslo.pyw -F -w -i pslo_icon.ico
~~~

编译完可能需要Wine或者Crossover才可以运行, 因此我们依旧推荐直接执行pyw文件或使用下一种方案

#### Nuitka (推荐)

请提前安装好**Visual Studio生成工具**或者**GCC(MinGW)**(使用MinGW需要在命令行添加`--mingw`)

运行......

~~~Bash
pip install nuitka
~~~

定位到代码根目录, 运行......

~~~Bash
nuitka pslo.pyw --onefile --windows-disable-console --windows-icon-from-ico=pslo_icon.ico --standalone --show-progress
~~~

适用于Windows和Linux, 参数可以按需添加, 详见[此处](https://github.com/Nuitka/Nuitka/)

## 🗒️备注

经过测试, 在虚拟机下运行可能会造成非正常闪烁现象, 可能是flet库的驱动驱动兼容的问题

代码写的有点难看, 望各位大佬多多指导!

## 📦使用到的第三方项目

### 2.x 及更新版本

[flet-dev/flet](https://github.com/flet-dev/flet)

[asweigart/pyperclip](https://github.com/asweigart/pyperclip)

### 1.x

[Riverbank Computing PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
