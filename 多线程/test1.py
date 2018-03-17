import os
from multiprocessing import Process  # windows 上编写多线程,需要引入的模块
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

pid = os.getpid()


def run_proc(name):
    logger.info('子进程%s(%s)运行...', name, pid)


if __name__ == '__main__':
    logger.info('父进程%s', pid)
    p = Process(target=run_proc, args=('test',))
    logger.info('线程即将运行')
    p.start()
    p.join()
    logger.info('进程执行完毕')
