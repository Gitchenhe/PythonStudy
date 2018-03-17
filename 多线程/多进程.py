from multiprocessing import Pool
import os, time, random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

pid = os.getpid()


def long_time_task(name):
    logger.info('任务执行 %s(%s)...', name, pid)
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    logger.info('任务%s 执行 %0.2f 秒', name, (end - start))


if __name__ == '__main__':
    logger.info('父进程%s', pid)
    p = Pool()
    for i in range(3):
        p.apply_async(long_time_task, args=(str(i),))

    logger.info('等待所有子线程执行完毕')
    p.close()
    p.join()
    logger.info('线程执行完毕')
