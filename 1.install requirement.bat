@echo off

echo 本脚本会通过pip安装Pseudo localization Demo依赖（包括旧版）
echo 安装后才可以正常编辑代码或者编译到二进制
echo 请确保您安装的Python大于等d于3.7版本
echo 注：由于使用了pypi官方源，因此速度会比较慢 
echo -----------------------------------------------------------------------

pause

pip install flet
pip install pyperclip
pip install PyQt5
pip install pywin32
pip install pyinstaller

echo 如果您看到黄色字体警告，说明安装目录不在Path下，您可以正常编辑代码与运行，但没法编译
echo 请按照提示添加Path环境变量
echo 当然，没有提示可以不用操作

pause