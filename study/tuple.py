#!/usr/bin/python3

# 元组  tuple一旦初始化就不能修改
# tuple中如果包含list，list是可以改变的（不能改变是指指向不变）

classmates = ('Michael', 'Bob', 'Tracy')

classmates[0]

# 空元组
t = ()
# 单个元素的元组（否则会赋值为数值，因为（）被辨识为小括号）
t = (1,)

print(t)
