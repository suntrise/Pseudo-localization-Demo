import requests
from lib import log # 日志输出库
from lib import platform_check

# 预备输出
log.out(0, "PSLO Update Module ready...")

# 全局化变量
global api
global all_info
global latest_ver

# 获取系统平台
sys_platform = platform_check.os_platform()

# API更新
def update_api():
    # API定义
    global api
    api = requests.get("https://api.github.com/repos/suntrise/Pseudo-localization-Demo/releases", timeout = 10, verify = False) # SSL禁用
    log.out(0, "API Update")
    global all_info
    all_info = api.json() # 获取Json
    log.out(0, "API infomation get")

# 版本检查
def version_check(ver):
    update_api()
    global latest_ver
    latest_ver = all_info[0]['tag_name'] # 获取最新版本
    log.out(0, "Versions in the server" + latest_ver)
    log.out(0, "Comparing versions...\033[0m")
    if ver == latest_ver:
        return False
    else:
        return True

# 更新程序
def update(ver):
    # 主体
    update_api()
    log.out(0, "Testing...")
    try:
        response = api.text # 用于是否可以链接Github
        if version_check(ver) == False:
            log.out(0, "You are using the latest version")
            return "NUL"
        else:
            log.out(0, "Getting the change log...\033[0m")
            detail = all_info[0]['body'] # 获取更新日志
            log.out(0, "Change log: " + detail)
            log.out(0, "Checking if it is a pre-release version...")
            prerelease = all_info[0]['prerelease'] # 获取是否为预览版本
            prerelease_content = ""
            if prerelease == "false":
                prerelease_content = "\n \r## 注意\n \r 本版本为预发布版本, 可能存在稳定性问题!" # 内容添加
                log.out(0, "" + latest_ver + "is a pre-release version")
            sc_content = ""
            if sys_platform == "darwin":
                sc_content = "\n \r## 兼容性须知\n \r 您似乎在使用macOS, \n \r我们使用了CI/CD编译适用于macOS的版本, 由于没有测试设备, 可能存在稳定性问题" # 内容添加
            elif sys_platform == "unknow":
                sc_content = "\n \r## 源代码须知\n \r 您似乎在使用未知的擦偶哦在系统, \n \r我们为您提供了源代码包而非二进制, 注意查收!" # 内容添加
            upd_content = "- 当前版本: " + ver + "\n \r- 新版本: " + latest_ver + "\n \r## 详细信息\n \r" + detail  + prerelease_content + sc_content # 弹窗内容
            return upd_content
    except requests.exceptions.RequestException as e:
        log.out(2, "Check for update failure")
        return "ERR"

# 获取下载链接  
def get_link():
    if sys_platform == "windows" or sys_platform == "linux":
        download_url = "https://github.com/suntrise/Pseudo-localization-Demo/releases"
    elif sys_platform == "darwin":
        download_url = "https://github.com/suntrise/Pseudo-localization-Demo/actions"
    else:
        log.out(0, "Getting the download link...")
        download_url = all_info[0]['tarball_url']
        log.out(0, "It is seem that you are using BSD or any other OS, so we provide the source code of the program (tar)")
    log.out(0, "Link: " + download_url)
    return download_url