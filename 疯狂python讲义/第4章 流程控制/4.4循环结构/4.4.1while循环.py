count_i = 0
while count_i < 10:
    print("count_i:", count_i)
    count_i += 1
print("循环结束")

# 使用whlie循环遍历列表和元组
a_tuple = ('fkit', 'carzyit', 'Charlie')
i = 0
while i < len(a_tuple):
    print("元组:", a_tuple[i])
    i += 1
print("循环结束")
print("循环列表")
src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
# 定义保存整除3的元素
a_list = []
# 定义保存整除余1的元素
b_list = []
# 定义整除余2的元素
c_list = []
print("列表元素:", src_list)
while len(src_list) > 0:
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3的列表:", a_list)
print("除以3余1的列表:", b_list)
print("除以3余2的列表:", c_list)
