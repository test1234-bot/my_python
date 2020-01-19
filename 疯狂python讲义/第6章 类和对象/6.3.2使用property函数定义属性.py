'''
如果为Python定义了setter,getter等访问器方法,则可使用property()函数将它们定义成属性
property()函数的语法格式如下:
    property(fget=None,fset=None,fdel=None,doc=None)
'''


class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def setsize(self, size):
        self.width, self.height = size

    def getsize(self):
        return self.height, self.width

    def delsize(self):
        self.width, self.height = 0, 0

    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


print(Rectangle.size.__doc__)
help(Rectangle.size)
rect = Rectangle(4, 3)
print(rect.size)
rect.size = 9, 7
print(rect.width)
print(rect.height)
del rect.size
print(rect.height)
print(rect.width)
