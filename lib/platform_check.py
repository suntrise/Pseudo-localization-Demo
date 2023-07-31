import sys
from lib import log # 日志输出库

# 预备输出
log.out(0, "OS Platform Module ready...")

# 平台检查
def os_platform():
    if sys.platform.startswith('linux'):
        log.out(0, "Current OS is Linux")
        return "linux"
    elif sys.platform.startswith('win'):
        log.out(0, "Current OS is Windows")
        return "windows"
    elif sys.platform.startswith('darwin'):
        log.out(0, "Current OS is darwin(macOS)")
        return "darwin"
    else:
        log.out(0, "Unknow OS")
        return "unknow"