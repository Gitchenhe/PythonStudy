import time, threading
import time, threading, logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
blance = 0


def change_it(n):
    # 先存后取,结果应该为0
    global blance
    blance = blance + n
    blance = blance - n


def run_thread(n):
    for i in range(10000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t2.start()
t1.start()

t1.join()
t2.join()
logger.info('blance = %s', blance)
