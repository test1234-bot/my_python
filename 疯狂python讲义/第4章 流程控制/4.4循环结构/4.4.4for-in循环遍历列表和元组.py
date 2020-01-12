print("循环遍历元组")
a_tuple = ('crazyit', 'fkit', 'Charlie')
for ele in a_tuple:
    print("当前元素是:", ele)

print("循环遍历列表")
src_list = [12, 45, 3.4, 'a', 4, 56, 'crazyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1
print("总和:", my_sum)
print("平均数:", my_sum / my_count)

for ele in src_list:
    print("元素是:", ele)

a_list = [330, 1.4, 50, 'crazyit', -3.5]
for num in range(0, len(a_list)):
    print("第%d个元素是:%s" % (num, a_list[num]))

print("循环遍历字典")
my_dict = {'语文': 89, '数学': 87, '英语': 98}
print("++++++++使用items()遍历字典+++++++++")
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)

print("++++++++使用keys()遍历字典++++++++++")
for key in my_dict.keys():
    print("key:", key)
    print("value:", my_dict.get(key))

print("++++++++++使用values()遍历字典+++++++++")
for value in my_dict.values():
    print("value:", value)

b_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
statistics = {}
print(b_list)
for ele in b_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1

for ele, count in statistics.items():
    print("%s出现的次数是:%d" % (ele, count))

print(statistics)
