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
