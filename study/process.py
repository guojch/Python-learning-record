# 多进程 multiprocessing

import os

# getppid()获取父进程ID
# print('Process (%s) start...' % os.getpid())

# fork()创建子进程
# 调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回
# 子进程永远返回0
# pid = os.fork()
# print(pid)


# from multiprocessing import Process
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()  # join()方法可以等待子进程结束后再继续往下运行
#     print('Child process end.')

# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)  # 最多跑4个，所以会先输出task0,1,2,3。默认是cpu核数
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#     p.join()  # join()方法会等待所有子进程执行完毕
#     print('All subprocesses done.')


# 进程间通信
# python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
