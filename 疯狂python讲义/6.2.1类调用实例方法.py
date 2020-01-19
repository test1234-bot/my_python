def foo():
    print("全局空间的foo方法")
bar=20

class Bird:
    #定义bird空间的foo函数
    def foo(self):
        print("bird空间的foo函数")
    #定义bird空间的bar变量
    bar=200

foo()
print(bar)
Bird().foo()
print(Bird().bar)

class User:
    def walk(self):
        print(self,'正在慢慢的走')

User.walk('fkit')
u=User()
u.walk()