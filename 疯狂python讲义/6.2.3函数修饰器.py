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

print("++++++++++++++++++++++++++++")

def foo(fn):
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        print("fn.name:", fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))
    return bar
@foo
def my_test(a):
    print("==my_test函数==", a)


print(my_test)
my_test(10)
my_test(6, 5)


print("再论命名空间")

global_fn=lambda p:print("执行lambda表达式,p参数",p)
class Gategory:
    cate_fn=lambda p:print("执行lambda表达式,p参数",p)

#调用全局global_fn,为参数p传入参数值
global_fn('fkit')
g=Gategory()
g.cate_fn()