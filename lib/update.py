import requests
from lib import platform_check

# 预备输出
print("\033[0;34m[INFO] PSLO Update Module ready...\033[0m")

# 全局化变量
api = ""
all_info = ""

# 获取系统平台
sys_platform = platform_check.os_platform()

# API更新
def update_api():
    # API定义
    global api
    api = requests.get("https://api.github.com/repos/suntrise/Pseudo-localization-Demo/releases", timeout = 10, verify = False) # SSL禁用
    print("\033[0;34m[INFO] API Update\033[0m")
    global all_info
    all_info = api.json() # 获取Json
    print("\033[0;34m[INFO] API infomation get\033[0m")

# 更新程序
def update(ver):
    # 主体
    update_api()
    print("\033[0;34m[INFO] Testing...\033[0m")
    try:
        response = api.text # 用于是否可以链接Github
        print("\033[0;34m[INFO] Get API information\033[0m")
        custom_ver = all_info[0]['name'] # 获取最新版本
        print("\033[0;34m[INFO] Versions in the server" + custom_ver + "\033[0m")
        print("\033[0;34m[INFO] Comparing versions...\033[0m")
        if custom_ver == ver:
            print("\033[0;32m[DONE] You are using the latest version\033[0m")
            return "NUL"
        else:
            print("\033[0;34m[INFO] Getting the change log...\033[0m")
            detail = all_info[0]['body'] # 获取更新日志
            print("\033[0;34m[INFO] Change log: " + detail + "\033[0m")
            # print("\033[0;34m[INFO] Getting the publish time...\033[0m")
            # publish_date_utc = all_info[0]['published_at'] # 获取更新日期
            # print("\033[0;34m[INFO] Publish time: " + publish_date_utc + "\033[0m")
            print("\033[0;34m[INFO] Checking if it is a pre-release version...\033[0m")
            prerelease = all_info[0]['prerelease'] # 获取是否为预览版本
            prerelease_content = ""
            if prerelease == "false":
                prerelease_content = "\n \r## 注意\n \r 本版本为预发布版本, 可能存在稳定性问题!" # 内容添加
                print("\033[0;34m[INFO] " + custom_ver + "is a pre-release version\033[0m")
            sc_content = ""
            if sys_platform == "darwin" or sys_platform == "unknow":
                sc_content = "\n \r## 源代码须知\n \r 您似乎在使用macOS或其他操作系统, 我们没有给这些系统编译二进制文件, 所以我们为您直接提供源代码" # 内容添加
            # upd_content = "- 当前版本: " + ver + "\n \r- 新版本: " + custom_ver + "\n \r## 详细信息\n \r" + detail + "\n \r## 发布日期\n \r" + publish_date_utc + prerelease_content + sc_content # 弹窗内容
            upd_content = "- 当前版本: " + ver + "\n \r- 新版本: " + custom_ver + "\n \r## 详细信息\n \r" + detail  + prerelease_content + sc_content # 弹窗内容
            return upd_content
    except requests.exceptions.RequestException as e:
        print("\033[0;31m[ERROR] Check for update failure\033[0m")
        return "ERR"

# 获取下载链接  
def get_link():
    assets = all_info[0]['assets']
    print("\033[0;34m[INFO] Getting the download link...\033[0m")
    if sys_platform == "windows":
        download_url = assets[0]['browser_download_url'] # 获取下载链接
    elif sys_platform == "linux":
        download_url = assets[1]['browser_download_url']
    else:
        download_url = all_info[0]['tarball_url']
        print("\033[0;34m[INFO] It is seem that you are using macOS or any other OS, so we provide the source code of the program(tar)\033[0m")
    print("\033[0;34m[INFO] Link: " + download_url + "\033[0m")
    return download_url