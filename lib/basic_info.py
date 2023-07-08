# 预备输出
print("\033[0;34m[INFO] Basic Information ready...\033[0m")

# 基本信息
ver = "v4.0.2p"
author = "Suntrise (STR)"
auth_abbr = "STR"
title = "伪本地化演示程序 " + ver + " by " + auth_abbr
updmd = """
# 更新日志 (详见GitHub Releases)

# v4.0.2p - 2023.7.9

1. 修复了一些BUG.

# v4.0.1p - 2023.7.4

1. 细节优化.

## v4.0p - 2023.7.4

1. [开发者]功能函数已拆分;
2. 引入Mini模式;
3. 新增文本文件导入&保存;
4. 新增窗口透明度设置;
5. 检查更新优化.

## v3.5p - 2023.7.1

1. 细节优化;
2. 字符库扩充;
3. [开发者]新增命令行日志;
4. 历史记录支持显示时间.

## v3.4p - 2023.6.27

1. 新增元音重复.
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
about_text = "伪本地化演示程序 " + ver + "\n开发者: " + author +"\n贡献者、使用到的第三方项目详见 GitHub 项目仓库\n(https://github.com/suntrise/Pseudo-localization-Demo)" 
