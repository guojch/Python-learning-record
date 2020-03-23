import math


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


if 19 >= 18:
    pass  # 不加pass，会报错


# 其实函数返回多个值，是返回一个tuple，一个tuple可以省略括号，用多个变量接收一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(x=None):
    if x is None:
        x = []
    x.append('END')
    return x


# 可变参数
# 在函数内部，参数numbers接收到的是一个tuple，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc(1, 2)
calc()

nums = [1, 2, 3]
calc(*nums)


# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# 关键字参数

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# 命名关键字参数

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
