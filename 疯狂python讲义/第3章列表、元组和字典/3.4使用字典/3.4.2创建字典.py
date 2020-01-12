'''
创建字典
    既可以使用花括号创建，也可以使用dict()来创建

'''
sores = {'语文': 90, '数学': 49, '英语': 78}
print(sores)
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30): 'good', 30: 'bad'}
print(dict2)
print(dict2.get(30))
# 使用dict创建字典时,可以传入多个列表或元组参数作为key-value,每个列表或元组将被当成一个key-value对,因此这些列表或元组只能包含两个元素
vegetables = {('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)}
# 创建包含3个key-value对的字典
dict3 = dict(vegetables)
print(dict3)
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
dict4 = dict(cars)
print(dict4)
# 使用关键字创建字典
dict5 = dict(spinach=1.39, cabbage=2.59)
print(dict5)
