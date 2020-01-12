a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
print(a_tuple)
print("访问元组第一个元素：", a_tuple[0])
print("访问元组第二个元素：", a_tuple[1])
print("访问元组倒数第一个元素:", a_tuple[-1])
print("访问元组倒数第二个元素", a_tuple[-2])

# 子序列

print("访问第2个至第4个元素:", a_tuple[2:4])
print("访问倒数第3个至倒数第一个的元素:", a_tuple[-3:-1])
print("访问第2个至倒数第2个:", a_tuple[1:-2])
print("访问倒数第3个至第5个：", a_tuple[-3:4])
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("访问第3个至第9个元素，间隔为2:", b_tuple[2:8:2])
print("访问第3个至第9个，间隔为3:", b_tuple[2:8:3])
print("访问第3个至倒数第2个，间隔为2：", b_tuple[2:-2:2])

print("+++++++++++++++加法+++++++++++++++")
a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)
# 计算元组相加
sum_tuple = a_tuple + b_tuple
print(sum_tuple)
print(a_tuple)
print(b_tuple)
# 两个元组相加
print(a_tuple + (-20, -30))
a_list = [20, 30, 50, 100]
b_list = ['a', 'b', 'c']
# 计算列表相加
sum_list = a_list + b_list
print(sum_list)
print(a_list + ['fkit'])

print("++++++++++++乘法++++++++++++")
a_tuple = ('crazyit', 20)
# 执行乘法
mul_tuple = a_tuple * 3
print(mul_tuple)
a_list = [30, 'Python', 2]
mul_list = a_list * 5
print(mul_list)

print("++++++++长度、最大值和最小值+++++++++++++")
# 元素都是数值的元组
a_tuple = (29, 49, 13, 22, 33, 10, 4, 102)
print("元素都是数值，最大值：", max(a_tuple))
print("元素都是数值，最小值:", min(a_tuple))
print("元素都是数值，长度:", len(a_tuple))
b_tuple = (
    'crazyit', 'Codes', 'Hibernate', 'struts', 'Spring', 'Appium', 'Ruby', 'Seleinum', 'Java', 'C++', 'Python', 'fkit')
print("元素都是字符串，最大值:", max(b_tuple))
print("元素都是字符串，最小值:", min(b_tuple))
print("元素都是字符串，长度:", len(b_tuple))

# 序列封包和序列解包
'''
程序把多个值赋值给一个变量时，python会自动将多个值封装成元组，称为序列封包
程序允许将序列(元组或列表)直接赋值给多个变量，此时程序的各个元素会被依次赋值给每个变量(要求序列的元素个数和变更的个数相等)，称为序列解包
'''
# 序列封包
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1, 10, 2))
print(a_tuple)
# 序列解包
a, b, c, d, e = a_tuple
print(a, b, c, d, e)
print(b)
a_list = ['fkit', 'crazyit']
a_str, b_str = a_list
print(a_str, b_str)
first, secod, *rest = range(10)
print(first)
print(secod)
print(rest)
*begin, last = range(10)
print(begin)
print(last)
first, *middle, last = range(10)
print(first)
print(middle)
print(last)
