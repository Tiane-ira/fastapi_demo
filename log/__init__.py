import logging
import os
from logging import handlers

from config import CONF

level = CONF['log']['level']
logger = logging.getLogger()
logger.setLevel(level)

# %(name)s：Logger的名字
# %(levelno)s：打印日志级别的数值
# %(levelname)s：打印日志级别的名称
# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s：打印当前执行程序名
# %(funcName)s：打印日志的当前函数
# %(lineno)d：打印日志的当前行号
# %(asctime)s：打印日志的时间
# %(thread)d：打印线程ID
# %(threadName)s：打印线程名称
# %(process)d：打印进程ID
# %(message)s：打印日志信息
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 输出日志到文件
log_path = CONF['log']['path']
if not os.path.exists(log_path):
    os.makedirs(log_path)
log_name = f"{CONF['server']['name']}.log"
log_abs_name = f"{log_path}/{log_name}"

rotation = CONF['log']['rotation']
if rotation == "1":
    # 按天分割文件日志
    time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=log_abs_name, when='D', encoding='utf-8')
    time_rotating_file_handler.setLevel(level)
    time_rotating_file_handler.setFormatter(formatter)
    logger.addHandler(time_rotating_file_handler)
else:
    # 完整日志文件
    file_handler = logging.FileHandler(log_abs_name, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# 输出日志到控制台
console = CONF['log']['console']
if console == "1":
    import sys
    import io

    # 设置标准输出和标准错误的编码为UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def init_logger():
    pass
