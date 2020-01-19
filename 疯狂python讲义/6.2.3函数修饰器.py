'''
自定义函数装饰器
①将被修饰的函数(函数B)作为参数传给@符号引用的函数(函数A)
②将函数B替换(装饰)成第①步的返回值
'''


def funA(fn):
    print("A")
    fn()
    return 'kfit'


@funA
def funB():
    print('B')

print(funB)
