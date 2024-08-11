import logging
import time

# 创建一个logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 设置日志级别

# 创建一个handler，用于写入日志文件
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)  # 可以根据需要设置文件日志级别

# 创建一个handler，用于输出到控制台
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  # 可以根据需要设置控制台日志级别

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# 实时写入日志
# for i in range(5):
#     logger.info(f'Processing iteration {i}')
#     time.sleep(1)  # 延迟模拟实时操作

# 日志将在程序运行过程中实时写入文件和控制台