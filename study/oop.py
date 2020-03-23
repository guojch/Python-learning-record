class Student(object):
    # 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    # 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    __slots__ = ('name', 'score')

    def __init__(self, name, score):
        self.__name = name
        self.score = score
        # __开头是私有变量
        # __xx__这种是特殊变量，可以直接访问
        # _name 这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
        # 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
        # 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


a = Student('guo', 99)
a.print_score()
