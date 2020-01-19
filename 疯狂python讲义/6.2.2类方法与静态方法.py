'''
类方法和静态方法的区别：
    Python会自动绑定类方法的第一个参数,类方法的第一个参数(通常建议参数名为cls)会自动绑定到类本身
    但对于静态方法不会自动绑定
    类方法用@classmethod修饰;
    静态方法用@staticmethod修饰
'''

#下面代码示范了定义类方法和静态方法
class Bird:

    #使用@classmethod来标识类方法
    @classmethod
    def fly(cls):
        print("类方法fly：",cls)

    #使用@staticmethod来标识静态方法
    @staticmethod
    def info(p):
        print("静态方法info:",p)
#调用类方法,Bird类会自动绑定到第一个参数
Bird.fly();
#调用静态方法,不会自动绑定,因此程序必须手动绑定到第一个参数
Bird.info('fkit')
#创建对象
b=Bird()
'''
使用对象调用fly()方法,依然是用类进行调用,会自动绑定到第一个参数
'''
b.fly()
'''
使用对象调用info()方法，依然是用类进行调用,所以不会自动绑定到第一个
参数,需要手动进行绑定
'''
b.info('Charlie')