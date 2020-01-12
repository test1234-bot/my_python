user_name = 'Charlie'
user_age = 8
print("读者姓名:", user_name, "年龄:", user_age, sep="|")

# 设置end参数后，指定输出之后不再换行
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")

# file参数指定print()函数的输出目标，file参数的默认值为sys.stdout,该默认值代表了系统标准输出
f = open("demo.text", "w")  # 打开文件以便写入
print("沧海月明珠有泪", file=f)
print("蓝田日暖玉生烟", file=f)
f.close()
