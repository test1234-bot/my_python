'''
>：大于，如果前面的值大于后面的值，则返回True，否则返回False
>=:大于等于，如果前面的值大于等于后面的值，则返回True,否则返回False
<：小于，如果前面的值小于后面的值，则返回True,否则返回False
<=:小于等于，如果前面的值小于等于后面的值，则返回True,否则返回False
==:等于，如果前面的值等于后面的值，则返回True,否则返回False
!=:不等于，如果运算符前面的值不等于后面的值，则返回True,否则返回False
is:判断两个变量所引用的对象是否相同，如果相同则返回True
is not:判断两个变更所引用的对象是否不相同，如果不相同则返回True
'''

print("5是否大于4：", 5 > 4)
print("3的4次方是否大于或等于90.0:", 3 ** 4 >= 90.0)
print("20是否大于等于20.0：", 20 >= 20.0)
print("5和5.0是否相等:", 5 == 5.0)
print("True是否和False相等：", True == False)
print("1是否和True相等：", 1 == True)
print("0是否和False相等：", 0 == False)
print("True+False:", True + False)
print("False-True：", False - True)
import time

a = time.gmtime()
b = time.gmtime()
print("a和b是否相等:", a == b)
print("a和b是否是同一个对象:", a is b)
