'''
Python的逻辑运算符有如下3个：
and:与，前后两个操作数必须都是True才返回True,否则返回False
or:或，前后两个操作数中有一个是True，就返回True,否则返回False
not:非，只需要一个操作数，如果操作数为True,则返回False,如果操作数为False,则返回True
'''

print(not False)
print("5大于3 and 20.0>10:", 5 > 3 and 20.0 > 10)
print("4>5 or 'c'>'a':", 4 > 5 or "c" > "a")

bookName = "疯狂Python"
price = 79
version = "正式版"
if bookName.endswith("Python") and (price < 50 or version == "正式版"):
    print("打算购买这本Python图书")
else:
    print("不购买！，太贵了！")
