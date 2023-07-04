import sys

# 预备输出
print("\033[0;34m[INFO] OS Platform Module ready...\033[0m")

# 平台检查
def os_platform():
    if sys.platform.startswith('linux'):
        print("\033[0;34m[INFO] OS is Linux\033[0m")
        return "linux"
    elif sys.platform.startswith('win'):
        print("\033[0;34m[INFO] OS is Windows\033[0m")
        return "windows"
    elif sys.platform.startswith('darwin'):
        print("\033[0;34m[INFO] OS is darwin(macOS)\033[0m")
        return "darwin"
    else:
        print("\033[0;34m[INFO] Unknow OS\033[0m")
        return "unknow"