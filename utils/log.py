import logging
# 创建logger记录器
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# 创建一个控制台处理器，并将日志级别设置为debug

ch = logging.StreamHandler()

ch.setLevel(logging.DEBUG)

# 创建formatter格式化器
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将formatter 添加到ch处理器
ch.setFormatter(formatter)

# 将ch添加到logger
logger.addHandler(ch)
