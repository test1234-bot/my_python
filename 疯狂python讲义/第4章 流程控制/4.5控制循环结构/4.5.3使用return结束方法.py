def test():
    for i in range(10):
        for j in range(10):
            print("i的值是:%d,j的值是:%d" % (i, j))
            if j == 2:
                return
            print("return后的语句:",i)


test()


