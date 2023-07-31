import datetime

# 日志
def out(cata, info):
    if cata == 0:
        print("\033[0;34mINFO\033[0m | " + datetime.datetime.now().strftime('%H:%M:%S') + " | " + info)
    elif cata == 1:
        print("\033[0;32mDONE\033[0m | " + datetime.datetime.now().strftime('%H:%M:%S') + " | " + info)
    elif cata == 2:
        print("\033[0;31mERROR\033[0m | " + datetime.datetime.now().strftime('%H:%M:%S') + " | " + info)
    elif cata == 3:
        print("\033[0;33mWARN\033[0m | " + datetime.datetime.now().strftime('%H:%M:%S') + " | " + info)