from multiprocessing import Process, Queue
import os, time, random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 写数据进程执行的代码
def write(q):
    for value in range(10000):
        logger.info('put %s in to queue', value)
        q.put(value)
        #time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    while True:
        value = q.get(True)
        logger.info('GET %s from queue', value)


if __name__ == '__main__':
    # 父进程创建queue,并传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw
    pw.start()
    # 启动子进程pr
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是死循环,无法等待其结束,只能强行终止
    pr.terminate()
