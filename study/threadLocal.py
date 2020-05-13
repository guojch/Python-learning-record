# ThreadLocal 用来解决多线程下，局部变量传递麻烦的问题

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    # 可以理解为全局变量local_school是一个dict，里面存着不同线程对应的值
    std = local_school.student
    print('Hello, %s (in %s) \r\n' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name  # 每个Thread对它都可以读写student属性，但互不影响。
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
