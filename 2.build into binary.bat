@echo off

echo 本脚本会将Pseudo localization Demo编译为二进制文件，在开始之前，请确定...
echo 1. 使用“1.install requirement.bat”安装的依赖文件夹在Path环境变量内
echo 2. Python版本为3.7或更高版本
echo 3. 没有在其他目录打开该文件
echo 注：基于PyQt5的旧版不会进行编译
echo -----------------------------------------------------------------------

pause

pyinstaller pslo.pyw -F -w -i pslo_icon.ico

echo 若要查看编译后文件，请打开运行目录下的“dist”文件夹
echo 若您没有看到文件，并且运行过程中报错，请确定您的Python版本以及pypi包是否正确安装

pause