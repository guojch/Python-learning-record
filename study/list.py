#!/usr/bin/python3

# list 有序集合

classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)
classmates[1]
# 倒一，倒二元素
classmates[-1]
classmates[-2]

# 追加元素到末尾
classmates.append('Adam')
# 插入元素到指定位置
classmates.insert(1, 'Jack')
# 删除末尾的元素/指定索引的元素
classmates.pop()
classmates.pop(2)
# 替换
classmates[1] = 'Sarah'

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']


print(classmates)
