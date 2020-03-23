# 多线程

# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：


import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 名字仅仅在打印时用来显示，完全没有其他意义，默认Thread-1，Thread-2……
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

balance = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()  # 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，其他线程就继续等待直到获得锁为止。
        try:
            pass
        finally:
            # 释放锁
            lock.release()

# 缺点
# 1、加了锁，实际上只能以单线程模式执行，效率降低
# 2、由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
