import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('操作系统名称:%s', os.name)
pwd = os.path.abspath('.')
logger.info('程序绝对路径%s', pwd)
pwd = pwd + '/test'
if os.path.exists(pwd):
    os.rmdir(pwd)

os.mkdir(pwd)
os.rmdir(pwd)

print(pwd)
