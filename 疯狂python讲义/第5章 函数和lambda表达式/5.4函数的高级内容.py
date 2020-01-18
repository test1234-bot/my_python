'''
使用函数变量
'''
print("定义一个乘方的函数")
def paw(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result
my_fun = paw
print(my_fun(3, 4))

def area(width, height):
    return width * height
my_fun = area
print(my_fun(3, 4))

'''
使用函数作为函数形参
'''
# 定义函数类型的形参，其中fn是一个函数
def map(data, fn):
    result = []
    for e in data:
        result.append(fn(e))
    return result
def square(n):
    return n * n
def cube(n):
    return n * n * n
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result

data = [3, 4, 5, 9, 8]
print("原数据:", data)
print("计算数组的平方:", map(data, square))
print("计算数组的立方:", map(data, cube))
print("计算数组的阶乘:", map(data, factorial))

print("使用函数作为返回值")
def get_math_func(type):
    # 定义计算平方的函数
    def square(n):
        return n * n
    # 定义计算立方的函数
    def cube(n):
        return n * n * n
    # 定义一个阶乘的局部函数
    def factorial(n):
        result = 1
        for index in range(1, n + 1):
            result *= index
        return result
    # 返回局部函数
    if (type == 'square'):
        return square
    elif type=='cube':
        return cube
    else:
        return factorial
# 调用get_math_func()函数，程序返回一个嵌套函数
math_func = get_math_func('square')
print(math_func(5))
math_func = get_math_func('cube')
print(math_func(5))
math_func = get_math_func('')
print(math_func(5))

'''
局部函数与lambda表达式
lambda表达式：
    lambda [parameter_list]:表达式
    lambda x,y:x+y
    等于
    def add(x,y):
        :return x+y
'''
def get_math_fun(type):
    if type == 'square':
        return lambda n: n * n
    if type == 'cube':
        return lambda n: n * n * n
    else:
        return lambda n: (1 + n) * n / 2
math_fun = get_math_fun("square")
print(math_fun(5))
math_fun = get_math_fun('cube')
print(math_fun(5))
math_fun = get_math_fun('')
print(math_fun(5))
