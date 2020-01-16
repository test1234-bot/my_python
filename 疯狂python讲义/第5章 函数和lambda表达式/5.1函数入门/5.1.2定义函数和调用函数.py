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
