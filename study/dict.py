# 字典（无序）

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

d['Michael'] = 99

# 判断key存在
print('Thomas' in d)
d.get('Thomas')
d.get('Thomas', -1)

# 删除key
d.pop('Bob')
print(d)
