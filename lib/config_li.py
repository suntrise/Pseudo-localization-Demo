from config import *
from lib import log # 日志输出库
import json

# 尚未完成  WIP

# 预备输出
log.out(0, "Config Read and Write Module ready...")

# 读取配置文件
def read_config():
    with open("config.json", "r") as json_file:
        config = json.load(json_file)
    return config

# 更新配置文件
def update_config(config):
    with open("config.json", 'w') as json_file:
        json.dump(config, json_file, indent = 4)
    return None

# 写入配置文件
def loadin_config(category, item, value):
