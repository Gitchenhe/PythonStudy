# 多任务可以由多进程完成,也可以有一个进程内的多线程完成
# 线程是操作系统直接支持的执行单元,因此高级语言通常内置多线程支持,python也不例外, 并且python的线程是真正的posix thread, 而不是
# 模拟出来的线程. python的标准库提供了两个模块,thread和threading,thread是低级模块,threading是高级模块,对thread进行了封装.绝大数情况下,
# 我们只需要使用threading这个高级模块
import logging
import time, threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 启动一个线程,把一个函数传入并创建thread实例,然后调用start()开始执行


# 新线程执行的代码
def loop():
    logger.info('thread %s is running', threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        logger.info('thread %s >>> %s', threading.current_thread().name, n)
        time.sleep(1)
    logger.info('thread %s ended.', threading.current_thread().name)


logger.info('thread %s is running', threading.current_thread().name)
t = threading.Thread(target=loop, name='线程1')
t1 = threading.Thread(target=loop, name='线程2')
t.start()
t1.start()
t1.join()
t.join()
logger.info('thread %s ended', threading.current_thread().name)
