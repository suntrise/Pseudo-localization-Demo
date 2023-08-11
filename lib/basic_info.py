from lib import log # 日志输出库

# 预备输出
log.out(0, "Basic Information ready...")

# 基本信息
ver = "v4.51p"
author = "Suntrise (STR)"
auth_abbr = "STR"
title = "伪本地化演示程序 " + ver + " by " + auth_abbr
updmd = """
# 更新日志 (详见GitHub Releases)

## v4.5.1p - 2023.8.2

1. 修复了一些BUG

## v4.5p - 2023.8.1

1. UI大改;
2. 优化了部分功能;
3. 检查更新API更换为KGithub;
4. [开发者]控制台日志输出优化;
5. 保存支持自动添加文件后缀;
6. 保存伪本地化内容时允许保留原文; 
7. 修复了一些BUG.

## v4.2.1p - 2023.7.17

1. 细节优化.

## v4.2p - 2023.7.15

1. 修复了一些BUG;
2. 界面更新;
3. 新增窗口置顶;
3. 细节优化.

## v4.1.1p - 2023.7.14

1. 新增保存历史记录;
2. 细节优化.

## v4.1p - 2023.7.14

1. 新增前后缀配置;
2. 历史记录页面更新;
3. 新增隐藏控制字符;
4. 细节优化.
"""

# 定义内容
what_text = """
伪本地化(pseudo-localization, 语言环境 **qps-ploc, qps-plocm, qps-ploca, en-XA, en-XB**), 

是通过模拟本地化过程, 以有效地调查在本地化中出现的问题

_(如字符无法正常显示, 或因字符串过长而导致语段显示不完整等)_。

在伪本地化过程中, 英文字母会被替换为来自其他语言的重音符号和字符。

_(例如, 字母 a 可以被 **αäáàāāǎǎăăåå** 中的任何一个替换)_,

还会添加分隔符等以增加字符串长度。

例: “Windows Photo Gallery (Windows 照片库)”→“ [1iaT9][ Ẅĭпðøωś Þнôтŏ Ģάŀļєяÿ !!! !] ”

### 更多信息: 

- https://docs.microsoft.com/zh-cn/globalization/methodology/pseudolocalization

- https://zhuanlan.zhihu.com/p/613293858
"""
about_text = "伪本地化演示程序 " + ver + "\n开发者: " + author +"\n贡献者、使用到的第三方项目详见 GitHub 项目仓库\n(https://github.com/suntrise/Pseudo-localization-Demo)\nMade with ❤ for YOU!\n使用WTFPL许可协议开源 (不涉及使用到的第三方库)" 
