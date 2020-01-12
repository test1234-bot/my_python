'''
python循环可以使用else,当循环条件为False时,执行else语句
'''

count_i = 0
while count_i < 5:
    print("count_i小于5:", count_i)
    count_i += 1
else:
    print("count_id大于或等于5:", count_i)

a_list = [330, 1.4, 50, 'fkit', -3.5]
for ele in a_list:
    print('元素:', ele)
else:
    print('元素:', ele)

print('++++++++++循环嵌套++++++++++++++')
# 外层循环
for i in range(0, 5):
    j = 0
    while j < 3:
        print("i的值为%d,j的值为%d" % (i, j))
        j += 1

print("++++++++++for表达式+++++++++++")
a_range = range(10)
a_list = [x * x for x in a_range]
print(a_list)

b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)

c_generator = (x * x for x in a_range if x % 3 == 0)
print(type(c_generator))
for i in c_generator:
    print(i, end="\t")
print()
d_list = [(x, y) for x in range(5) for y in range(4)]
print(d_list)

src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
src_c = [(a, b) for a in src_a for b in src_b if a % b == 0]
print(src_c)

print("+++++++++++++++++++")
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = [x for x in zip(a, b)]
print(c)
print(type(c))
