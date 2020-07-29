#!/usr/bin/python3

# 元组  tuple一旦初始化就不能修改
# tuple中如果包含list，list是可以改变的（不能改变是指指向不变）
# 列表和元组的区别在于：列表可以增删数据

classmates = ('Michael', 'Bob', 'Tracy')

classmates[0]

# 空元组
t = ()
# 单个元素的元组（否则会赋值为数值，因为（）被辨识为小括号）
t = (1,)

print(t)

# 元组比较
print((4,) > (5,))  # 单独的数字比较
print((1, 20) < (2, 20))  # 当作120>220比较
