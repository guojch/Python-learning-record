# 变量可以指向函数，函数名也是变量
abs = 10


# abs(-10)


# 就无法通过abs(-10)调用该函数了
# 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数


# map
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
r = list(r)
print(r)
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。


# 把这个list所有数字转为字符串
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 效果：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# filter 函数用于过滤序列。
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

# sorted

sorted([36, 5, -12, 9, -21])
# 它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
sorted([36, 5, -12, 9, -21], key=abs)
# 字符串排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
sorted(['bob', 'about', 'Zoo', 'Credit'])
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写）
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)