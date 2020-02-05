print("{},{} and {}".format("first", "second", "third"))
print("{0},{1} and {2}".format("First", "Second", "Third"))

# 使用索引可以不用排序
print("{3} {0} {2} {1} {3} {0}".format('be', 'not', 'or', 'to'))

# 宽度、精度和千位分隔符
# 右对齐并且保持10位
print("{num:10}".format(num=3))

print("Pi day is {pi:.2f}".format(pi=3.14))
print("Pi day is {pi:10.2f}".format(pi=3.14))
print("{:010.2f}".format(3.14))
# 指定左对齐，右对齐和居中可以使用<,>,^
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f"
      "}".format(3.14))
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(3.14))

#使用指定的字符来填充而不是空格
print("{:$^15}".format(" WIN BIG "))
print("{:^15}".format(" WIN BIG "))