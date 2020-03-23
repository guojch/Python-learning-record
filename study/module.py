# 模块module
# 包package

# mycompany 包名
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

# 可以有多级目录，组成多级层次的包结构。

print(__name__)
# 当我们在命令行运行模块文件时，Python解释器把一个特殊变量__name__置为__main__

# 作用域
# 通过_前缀来实现的

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
