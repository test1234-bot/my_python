s = ""
if s:
    print("s不是空字符串")
else:
    print("s是空字符串")

s_age = input("请输入年龄:")
age = int(s_age)
if age >= 20:
    print("年龄已经大于20岁了")
    print("20岁以上的人应该学会承担责任")

b = 3
if b > 4:
    print("b大于4:", b)
else:
    b -= 1
    print("b不大于4:", b)
