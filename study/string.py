#!/usr/bin/python3

print('hello world')

# 输出多行
print('''line1
line2
line3''')

# 格式化
print('Hello %s' % 'world')
print('Hello %s AND %s AND %s %% AGE %d-%5d-%05d %.3f' % ('xiaoming', 'xiaohong', 610, 22, 22, 22, 1.11))

# 切片操作符 [:]
# 连接操作符 +
# 重复操作符 *
# 成员关系操作符 in、not in
# 字符串/数组/元组都属于序列，都有上述4个操作符
a = '我是胡二筒'
print(a[0])
print(a[-1])
print(a[1:3])
print('二' in a)
print('二' not in a)
print(a + '66')
print(a * 3)
