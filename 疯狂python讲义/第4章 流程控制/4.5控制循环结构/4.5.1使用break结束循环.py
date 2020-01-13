print("简单的for循环")
for i in range(0, 10):
    print("i的值：", i)
    if i == 2:
        break

print("+++++++++++++++")
exit_flag = False
for i in range(0, 10):
    for j in range(0, 5):
        print("i的值是:%d,j的值是:%d" % (i, j))
        if j == 3:
            exit_flag = True
            break
    if exit_flag:
        break

