# 创建列表
a_tuple = ('crazyit', 20, -1.2)
print("将元组转换成列表:", list(a_tuple))
a_range = range(1, 5)
print(a_range)
b_list = list(a_range)
print("将区间转换成列表:", b_list)
c_list = list(range(4, 20, 3))
print(c_list)

# 增加列表元素
a_list = ['crazyit', 20, -2]
a_list.append('fkit')
print(a_list)
a_tuple = (3.4, 5.6)
a_list.append(a_tuple)
print("a_list列表所加元组a_tuple：", a_list)

b_list = ['a', 30]
b_list.extend((-2, 3.1))
print("追加元组中的所有元素:", b_list)
b_list.extend(['C', 'R', 'A'])
print("b_list", b_list)
# 追加区间的所有元素
b_list.extend(range(97, 100))
print("b_list", b_list)
c_list = list(range(1, 6))
print("c_list", c_list)
# 在索引3处插入字符
c_list.insert(3, 'Crazyit')
print(c_list)
# 在索引3处插入元组，元组会被当成一个元素
c_list.insert(3, tuple('Crazyit'))
print(c_list)
c_list.insert(3, ('fkit', 'Python'))
print(c_list)

# 删除元素
print("++++++++++++删除元素++++++++++++++")
del c_list[3]
print(c_list)
del c_list[1:3]
print(c_list)
# del c_list

# remove删除第一个找到的元素，没找找到报错ValueError
c_list.remove(4)
print(c_list)
c_list.clear()
print(c_list)
# 修改元素
a_list = [2, 4, -3.4, 'crazyit', 23]
print("修改前元素:", a_list)
a_list[2] = 'fkit'
print("修改元素-a_list[2]='fkit'", a_list)
a_list[-2] = 9876
print("修改元素-a_list[-2]=9876", a_list)
b_list = list(range(1, 5))
print("修改元素-b_list== list(range(1, 5))", b_list)
b_list[1:3] = ['a', 'b']
print("修改元素-b_list[1:3]= ['a', 'b']", b_list)
# 将第3个至第3个(不包含)元素赋值为新列表的元素，就是插入元素
print("b_list:", b_list)
b_list[2:2] = ['x', 'y']
print("b_list[2:2] = ['x', 'y']:>", b_list)
b_list[2:5] = []
print("b_list[2:5] = []:>", b_list)
c_list = list(range(1, 10))
# 指定step为2，被赋值的元素有4个，因此用于赋值的列表也必须有4个元素
c_list[2:9:2] = ['a', 'b', 'c', 'd']
print("c_list[2:9:2] = ['a', 'b', 'c', 'd']:>", c_list)

# 列表的其他常用方法
print(dir(list))
'''
count():用于统计列表中某个元素出现的次数
index():用于判断某个元素在列表中出现的位置
pop():用于寺将列表当成“栈”使用，实现元素出栈功能
reverse():用于将列表元素反向存放
sort():用于对列表元素排序
'''

a_list = [2, 30, 'a', [5, 23, -1], 30]
print("查看列表中30出现的次数:", a_list.count(30))
print("查看列表中[5,23,-1]出现的次数:", a_list.count([5, 23, -1]))
print("查看30在列表中的索引:", a_list.index(30))
print("从索引2开始查看30在列表中的索引：", a_list.index(30, 2))
print("从索引2至4之间查看30在列表中的索引:", a_list.index(30, 2, 5))

# 栈
stack = []
# 向栈中插入3个元素
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")
print(stack)
# 最后入栈的元素被移出栈
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# 列表元素反转
a_list = list(range(1, 10))
print("反转前列表元素:", a_list)
# 列表反转方法
a_list.reverse()
print("反转后列表元素:", a_list)

# 列表倒序方法
a_list.sort()
print("列表倒序:", a_list)
b_list = [2, 4, 34, 12, -23, -1, 56, 0, 3.4, -1.2]
print("排序前：", b_list)
# 倒序
b_list.sort()
print(b_list)
b_list.sort(reverse=True)
print(b_list)
c_list = ['Python', 'Go', 'Ruby', 'Kotlin', 'Erlang', 'Swift']
c_list.sort()
print(c_list)
# 按元素字符长度进行排序,默认为从小到大
c_list.sort(key=len)
print(c_list)
# reverse=True时从大到小
c_list.sort(key=len, reverse=True)
print(c_list)
c_list.sort(key=max)
print(c_list)
