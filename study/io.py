# try:
#     f = open('/Users/guojch/python/study/input.py', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()  # 1、占用资源  2、同一时间能打开的文件数量也是有限的
#
# # Python引入了with语句来自动帮我们调用close()方法：
# with open('/Users/guojch/python/study/input.py', 'r') as f:
#     print(f.read())
# # 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
#
# print('---------------')
#
# # 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# # 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
# # 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
# with open('/Users/guojch/python/study/input.py', 'r') as f:
#     print(f.readline())
#
# with open('/Users/guojch/python/study/input.py', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())  # 把末尾的'\n'删掉
#
# print('---------------')
#
# # 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
# f = open('/Users/guojch/Downloads/bg.jpg', 'rb')
# print(f.read())
# f.close()
#
# # 写文件
# f = open('/Users/guojch/python/study/test.py', 'a')
# f.write('Hello, world!')
# f.close() # write不一定会立即写入，先在内存中，空闲时候再写入，只有调用了close，才会全部写入
# # 所以还是用with比较保险
# with open('/Users/guojch/python/study/test.py', 'a') as f:
#     f.write('Hello, world!')

import os

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中


import json
d = dict(name='Bob', age=20, score=88)
d_json = json.dumps(d)
print(d_json)
print(json.loads(d_json))