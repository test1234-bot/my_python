'''
for-in循环用于遍历范围,列表,元素和字典等可迭代对象包含的元素
for-in循环的语法格式如下:
    for 变量 in 字符串|范围|集合等:
        statements

'''

s_max = input("请输入您想计算的阶乘:")
mx = int(s_max)
reslut = 1
for num in range(1, mx + 1):
    reslut *= num
print(reslut)
