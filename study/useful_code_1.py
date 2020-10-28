"""
在两个变量之间交换值
"""
a = 5
b = 10
a, b = b, a
# print(a, b)

"""
查找对象使用的内存
"""
import sys

# print(sys.getsizeof(5))
# print(sys.getsizeof("Python"))

"""
反转字符串
    Python 字符串库不像其他 Python 容器（如 list) 那样支持内置的 reverse()。
    a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
"""
language = "python"
reversed_language = language[::-1]
# print(reversed_language)

"""
打印字符串n次
"""
# print('python' * 3)

"""
将字符串列表合并为单个字符串
"""
strings = ['50', 'python', 'snippets']
# print(','.join(strings))

"""
查找存在于两个列表中任一列表存在的元素（集合）
"""
a = [1, 2, 3, 4, 5]
b = [6, 2, 8, 1, 4]
# print(list(set(a + b)))

"""
查找给定列表中的所有唯一元素（集合过滤重复元素）
"""
numbers = [1, 2, 3, 2, 4]
# print(list(set(numbers)))

"""
跟踪列表中元素的频率
"""
from collections import Counter

list = [1, 2, 3, 2, 4, 3, 2, 3]
count = Counter(list)
# print(count)

"""
查找列表中出现频率最高的元素
"""
numbers = [1, 2, 3, 2, 4, 3, 1, 3]
# print(max(set(numbers), key=numbers.count))

"""
使用函数链式调用
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 5, 10
# print((subtract if a > b else add)(a, b))
