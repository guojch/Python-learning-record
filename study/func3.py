# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f, f())

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1 == f2  # False  f1()和f2()的调用结果互不影响。


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())  # 结果不是1 4 9 而是 9 9 9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 匿名函数
lambda x: x * x


# 关键词lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 等效于

def f(x):
    return x * x


fName = f

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(fName.__name__)


# 装饰器
# 假设我们要增强函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log  # 相当于执行了 now = log(now) , 调用now()将执行新函数
def now():
    print('2000-01-01')


now()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log(
    'execute')  # 相当于执行了 now = log('execute')(now)，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
def now():
    print('2015-3-25')


# 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# 所以完整的写法是：
import functools


def log(func):
    @functools.wraps(func)  # wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 偏函数
# functools.partial就是帮助我们创建一个偏函数的
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
