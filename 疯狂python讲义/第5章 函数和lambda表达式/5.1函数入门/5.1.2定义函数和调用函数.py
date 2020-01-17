'''
def 函数名(形参列表):
    执行语句
'''


def may_max(x, y):
    z = x if x > y else y
    return z


def sai_hello(name):
    print("==正在执行say_hello()函数")
    return name + "你好！"


a = 8
b = 9
result = may_max(a, b)
print("result:", result)
print(sai_hello("Testa！！！！"))
print("多个返回值")


def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
ls = sum_and_avg(my_list)
print(ls)

print("++++++++++++递归函数++++++++++++++")


def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n - 1) + fn(n - 2)


print(fn(10))

print("++++++++++关键字参数++++++++++++")


def girth(width, height):
    print("width:", width)
    print("height", height)
    return 2 * (width + height)


print("根据位置传入参数:", girth(3.5, 4.8))
print("根据关键字传入参数:", girth(width=3.5, height=4.8))
print("关键字参数可以交换位置:", girth(height=4.8, width=3.5))
print("部分位置参数，部分关键字参数:", girth(3.5, height=4.8))

print("+++++++参数默认值++++++++++++")
'''
语法格式：
    形参名=默认值
'''


def say_hi(name='孙悟空', message="欢迎学习Python"):
    print(name, "你好！")
    print("消息是：", message)


print("全部使用默认参数:")
say_hi()
print("message使用默认参数：")
say_hi('唐僧')
print("都不使用默认值:")
say_hi('白骨精', '欢迎深入学习Python')
print("只有name使用默认值:")
say_hi(message="欢迎了解使用Python！")

print("定义一个打印三角形的函数")


def printTriangle(char, height=5):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(' ', end="")
        for j in range(2 * i - 1):
            print(char, end='')
        print()


printTriangle('@', 6)
printTriangle('#', height=7)
printTriangle(char='*')

print("+++++++++参数收集++++++++++")


# 定义了支持参数收集的函数
def test(a, *books):
    print("books:", books)
    for b in books:
        print("b:", b)
    print("a:", a)


test(5, '疯狂Python讲义', '疯狂Android讲义')


# 可变的形参可以处于形参列表的任意位置
def test1(*books, a):
    print("books:", books)
    for b in books:
        print("b:", b)
    print("a:", a)


test('疯狂Python学习', '疯狂Java学习', '回家了', 190)


# Python收集关键字参数收集字典
def test2(x, y, z=3, *books, **scores):
    print("x,y,z:", x, y, z)
    print("books:", books)
    print("scores:", scores)
    for k, v in scores.items():
        print("k,v", k, v)


test2(1, 2, '疯狂Python讲义', '疯狂Java讲义', 语文=90, 数学=89, 英语=97)

print("++++++++++逆向参数收集+++++++++++")


def test3(name, message):
    print("name:", name)
    print("message:", message)


# 逆向收集参数需要在传入的列表、元组参数之前添加一个星号,在字典参数之前添加两个星号
my_list = ['孙悟空', '欢迎来到疯狂Python学习']
test3(*my_list)


def test4(name, *nums):
    print("name:", name)
    print("nums参数:", nums)


my_tuple = (1, 2, 3)
test4('fkit', *my_tuple)


# 字典也支持逆向收集
def bar(book, price, desc):
    print("book:", book)
    print("price:", price)
    print("desc:", desc)


my_dict = {'book': '疯狂Python讲义', 'price': 90, 'desc': '这是一本系统全面的Python学习教程'}

bar(**my_dict)

print("+++++++++++函数的传递机制+++++++++")


def swap(a, b):
    # 交换a,b的值
    a, b = b, a
    print("swap函数里,a的值是:", a, ": b的值是：", b)


a = 6
b = 9
swap(a, b)
print('交换结束后,a的值是:', a, ":b的值是：", b)
