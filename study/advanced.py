# 1、切片

# 2、迭代
# 默认迭代的是key，
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# print(d.values())
# print(d.items())
# 迭代value
for value in d.values():
    print(value)
# 同时迭代key和value
for k, v in d.items():
    print(k, v)

# 还能迭代字符串呢
for ch in 'XYZ':
    print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 还能这样
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 3、列表生成式
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名
import os

print([d for d in os.listdir('.')])

# 循环key,value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 将list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
[x for x in range(1, 11) if x % 2 == 0]
[x if x % 2 == 0 else -x for x in range(1, 11)]

# 4、生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 在Python中，一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。
# 第一种：只要把一个列表生成式的[]改成()
g = (x * x for x in range(10))

print(g)
# print(next(g), next(g))
for n in g:
    print(n)


# tip: 赋值语句
# a, b = b, a + b
# 相当于
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 函数：遇到return或者最后一行函数语句就返回
# generator：遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections.abc import Iterable

isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)

from collections.abc import Iterator

isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
isinstance({}, Iterator)
isinstance('abc', Iterator)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print('-------')
print(iter([]))
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

