'''
列表除使用索引来访问单个元素外,还可使用切片来访问特定范围内的元素。
'''
tag = '<a href="http://www.python.org">Python web site</a>'
print("tag[9:30]:", tag[9:30])
print("tag[32:-4]:", tag[32:-4])
print("tag[1:1]:", tag[1:1])
print("tag[-3:]:", tag[-3:])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])
print(numbers[-3:])
print(numbers[-3:-1])
print("复制整个列表:", numbers[:])
url = "http://www.baidu.com"
print("提取url域名:", url[11:-4])
ls = []
for i in range(1, 11):
    ls.append(i)
print(ls)
print("步长为1:", ls[0:10:1])
print("步长为2:", ls[0:10:2])
print("步长为2:", ls[0:10:3])
print("步长为2:", ls[0:10:4])

# 列表相加
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 修改列表
x = [1, 1, 1]
x[1] = 2
print(x)

# 删除元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
print("删除前列表元素:", names)
del names[2]
print("删除后列表元素:", names)

# 给切片赋值
name = list('Perl')
print("切片赋值前:", name)
name[2:] = list('China')
print("切片赋值后:", name)

# 使用切片赋值可以插入元素
name[1:1] = [2, 3, 4]
print("使用切片元素插入元素：", name)
# 使用切片删除元素
name[1:4] = []
print("使用切片赋值删除元素:", name)

#列表方法
#append()
lst=[1,2,3]
print("增加前的列表:",lst)
lst.append('aa')
print("增加后的列表:",lst)

#清空列表-clear
lst.clear()
print("执行clear后的列表：",lst)

#复制列表-copy
a=[1,2,3]
b=a
print(b)
b[1]=4
print(b,a)
c=a.copy();
b[2]=5
print(a,b,c)

d=[3,1,4,7,3,0]
d.reverse()
print(d)
d.sort(reverse=True)
print(d)