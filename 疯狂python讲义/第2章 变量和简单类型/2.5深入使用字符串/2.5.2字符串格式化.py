price = 108
'''
字符串中的%s是一个占位符，第二个%固定使用"%"作为分隔符
'''
print("the book's price is %s" % price)
user = "Charlie"
age = 8
print("%s is a %s years old boy" % (user, age))
num = -28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6s" % num)

'''
-：表示左对齐
+：表示数值总是要带着符号(正数带"+",负数带"-")
0:表示不补充空格，而是补充0
'''

print("最小宽度为0，左补0")
num2 = 30
print("num2 is:%06d" % num2)
print("最小宽度为6,左边补0，总带上符号")
print("num2 is:%+06d" % num2)
print("最小宽度为6，左对齐")
print("num2 is:%-6d" % num2)

print("====================")
my_value = 3.001415926535
# 最小宽度为8，小数点后只留3位
print("my_value is:%8.3f" % my_value)
# 最小宽度为8,小数点后保留3位，左边补0
print("my_value is:%08.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0，始终带符号
print("my_value is:%+08.3f" % my_value)

the_name = 'Charlie'
# 只保留3个字符
print("the name is %.3s" % the_name)
# 只保留2个字符，最小宽度为10
print("the name is %10.2s" % the_name)
