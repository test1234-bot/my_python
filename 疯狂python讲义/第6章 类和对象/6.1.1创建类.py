'''
创建Person类
'''


class Person:
    # 定义一个变量
    hair = 'black'

    def __init__(self, name='Charlie', age=8):
        # 为Person对象增加两个实例变量
        self.name = name
        self.age = age

    def say(self, context):
        print(context)


p = Person()
p.say('这是一个Python类方法')
print(p.name, p.age)
# 访问实例变量，并直接赋值
p.name = 'Test'
# 增加类变量
p.tilte = '这是一个类Title变量'
print(p.name, p.age, p.tilte)


# 定义一个函数
def info(self):
    print("----------info函数----------", self)


p.info = info
p.info(p)

# 使用lambda表达式
p.bar = lambda self: print('------------info函数-------------', self)
p.bar(p)


# 自动绑定到第一个参数,借助于types模块下的MethodType进行包装
def intro_func(self, content):
    print("我是一个人,信息是:%s" % content)


# 导入MothodType包
from types import MethodType

# 使用MethodType对intro_func函数第一个参数绑定为p
p.intro = MethodType(intro_func, p)
p.intro("生活在不自由中")


# 实例方法自动绑定self
class Dog:
    # 定义一个jump()方法
    def jump(self):
        print("正在调用jump方法")

    # 定义run方法
    def run(self):
        # 使用self参数调用jump方法
        self.jump()
        print("正在执行run方法")
d = Dog()
d.run()
