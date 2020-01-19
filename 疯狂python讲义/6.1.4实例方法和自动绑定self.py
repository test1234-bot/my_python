class InConstructor:
    def __init__(self):
        foo = 0
        self.foo = 6


print(InConstructor().foo)


class User:
    def test(self):
        print("self参数：", self)


u = User()
u.test()
foo=u.test()
foo

