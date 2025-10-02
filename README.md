# 🌐伪本地化演示程序

![截图](https://user-images.githubusercontent.com/89229642/255376854-128a04f0-cf92-4408-b74c-17d6ae7d66f8.png)

这是一个伪本地化工具, 可用于某些本地化工作用途, 当然也可以作为一个玩具或者工具~

![GitHub Action](https://github.com/suntrise/Pseudo-localization-Demo/actions/workflows/build.yml/badge.svg)
![GitHub repo stars](https://img.shields.io/github/stars/suntrise/Pseudo-localization-Demo)
![GitHub repo contributors](https://img.shields.io/github/contributors/suntrise/Pseudo-localization-Demo)
![GitHub repo license](https://img.shields.io/github/license/suntrise/Pseudo-localization-Demo)
![GitHub issues](https://img.shields.io/github/issues/suntrise/Pseudo-localization-Demo)
![GitHub release](https://img.shields.io/github/v/release/suntrise/Pseudo-localization-Demo)
![GitHub download counts](https://img.shields.io/github/downloads/suntrise/Pseudo-localization-Demo/total)
![GitHub repo size](https://img.shields.io/github/repo-size/suntrise/Pseudo-localization-Demo)
![Python requirement](https://img.shields.io/badge/python-≥3.7-brightgreen?logo=python)


网页版：https://suntrise.github.io/pseudo

## 👇使用

如果您没有Python环境且比较懒, 可以移步 [Release](https://github.com/suntrise/Pseudo-localization-Demo/releases) 下载, tar.gz 版本适用于 Linux, exe 版本适用于 Windows, 其他操作系统建议下载源码并执行 (macOS 版用户可以到 [Actions 页](https://github.com/suntrise/Pseudo-localization-Demo/actions)下载)

注意, 要在本地查看并修改源码, 需要安装 Python, 版本最少为 3.10 以保障兼容性

### 🚀 依赖安装

#### 🧩 Poetry 安装

本项目使用 `poetry` 进行依赖管理, 请务必先安装它, 并将其添加在 `PATH` 环境变量中!

安装指南详见: https://python-poetry.cn/docs/#installation

##### 通用

如果您已经安装了 `pipx` 则可以执行...

~~~bash
pipx install poetry
~~~

##### Windows

您可以在 PowerShell 中执行...

~~~powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
~~~

> 如果您通过 Microsoft Store 安装了 Python, 请在上面的命令中将 `py` 替换为 `python`

##### *nix

在安装了 `curl` 的前提下执行...

~~~bash
curl -sSL https://install.python-poetry.org | python3 -
~~~

##### macOS

如果您不喜欢使用上面 `curl` 的方式, 如果已经安装了 Homebrew, 可以执行...

~~~
brew install --formula poetry
~~~

#### 🗿正式依赖安装

创建完虚拟环境后运行...

~~~Bash
poetry install
~~~

它将会自动安装需要的依赖

### 🛠️编译



## 🗒️备注

- 经过测试, 在虚拟机下运行可能会造成非正常闪烁现象, 可能是flet库的驱动驱动兼容的问题

- 以上命令可能会有些许滞后, 若编译效果不佳, 可参考 Workflow 脚本进行参数补充

- 若想获取最新测试版本, 可以看看 Action 里面哟(未经过完整测试)

- 代码写的有点难看, 望各位大佬多多指导!

## 📦 使用到的第三方项目

### 2.x 及更新版本

[flet-dev/flet](https://github.com/flet-dev/flet)

[pypi/fleter](https://pypi.org/project/fleter) (最新版本已弃用)

[asweigart/pyperclip](https://github.com/asweigart/pyperclip)

## 📄 许可协议

使用 **WTFPL** 许可协议开源[^1], 你想干嘛就干嘛

![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)

[^1]: 或许可以解释为**W**indows **T**iny **F**orm **P**seudo-**L**ocalization
