print("九九乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(j, i, i * j), end="")
    print()

print("循环输出等腰三角形")

n = 5
for i in range(1, n):
    for j in range(n - i):
        print("-", end="")
    for x in range(2 * i - 1):
        print("*", end="")
    print()

print("循环输出菱形")

n = 5
for i in range(1, n):
    for j in range(n - i):
        print("-", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for a in range(1, n):
    for b in range(1, a + 1):
        print("-", end="")
    for c in range(2 * a - 1):
        print("*", end="")
    print()

# 打印菱形
print("打印空心等菱形，这里去掉if-else条件判断就是实心的")

rows = 5
for i in range(rows):  # 变量i控制行数
    for j in range(rows - i):  # (1,rows-i)
        print(" "),
        j += 1
    for k in range(2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2:
            print("*")
        else:
            print(" ")
        k += 1
    print("")
    i += 1
    # 菱形的下半部分
for i in range(rows):
    for j in range(i):  # (1,rows-i)
        print(" "),
        j += 1
    for k in range(2 * (rows - i) - 1):  # (1,2*i)
        if k == 0 or k == 2 * (rows - i) - 2:
            print("*"),
        else:
            print(" "),
        k += 1
    print()
    i += 1
