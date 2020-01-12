'''
基本操作方法如下:
    通过key访问value
    通过key添加key-value对.
    通过key删除key-value对.
    通过key修改key-value对.
    通过key判断指定key-value对是否存在.
    通过key访问value也是使用方括号语法
'''
scores = {'语文': 89}
# 通过key访问value
print(scores['语文'])
# 对不存在的key赋值,就是添加key-value
scores['数学'] = 90
print(scores)

# 删除key-value,使用del
del scores['语文']
print(scores)

# 对已存在的key赋值,会覆盖旧值
scores['数学'] = 99
print(scores)

# 使用in判断字典是否包含指定的key
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 3.8}
print("判断cars是否包含'AUDI'的key:", 'AUDI' in cars)
print("判断cars是否包含名为PORSCHE的key:", 'PORSCHE' in cars)
print("判断cars是否不包含名为PORSCHE的key:", 'PORSCHE' not in cars)

print("++++++++++字典常用的方法++++++++++++")
print(dir(dict))
'''
clear():用于清空字典中所有的key-value,该字典会变成一个空字典
'''
print(cars)
cars.clear()
print(cars)

# get()方法是根据key来获取value,它相当于方括号语法的增强版,当使用方括号获取不存在的key时,会报KeyError;使用get()访问不存在的key时,该方法会返回None
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 3.8}
print(cars.get('BMW'))
print(cars.get('PORSCHE'))
# print(cars['PORSCHE'])

# update()方法使用一个字典所包含的key-value对来更新已有的字典,在执行
print(cars)
cars.update({'BMW': 9.0})
print("使用update更新已存在的key:", cars)

cars.update({'YY': 1.8})
print("使用update更新不存在的key:", cars)

# 获取字典中所有的key-value对,返回一个dict_items对象
ims = cars.items()
print(ims)
print(type(ims))
print(list(ims))
print("访问第2个key-value对", list(ims)[1])

kys = cars.keys()
print("获取字典中所有的key:", kys)
print(type(kys))
print(list(kys))
# 访问第2个key
print("访问第2个key:", list(kys)[1])
vals = cars.values()
print("获取字典中所有的values对象:", vals)
print(type(vals))
print(list(vals))
print("访问第2个value:", list(vals)[1])
print("使用pop()指定删除key-value:", cars.pop('AUDI'))
print(cars)
print('使用popitem()方法,删除随机key-value:', cars.popitem())
print(cars)
k, v = cars.popitem()
print(k, v)

print("使用setdault()方法:", cars.setdefault('AUDI', 8.6))
print(cars)
print(cars.setdefault('BMW', 9.9))
print(cars)
# 使用列表创建包含两个key的字典
a_dict = dict.fromkeys(['a', 'b', 'c', 'd'])
print(a_dict)
# 使用元组创建字典
b_dict = dict.fromkeys(('e', 'f', 'g', 'h'))
print(b_dict)
# 使用元组创建包含两个key的字典,指定默认value
c_dict = dict.fromkeys((1, 2), 'good')
print(c_dict)

# 在字符串模板中使用key
temp = '书名是:%(name)s,价格是:%(price)010.2f,出版社是:%(publish)s'
book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子书'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {"name": "疯狂Kotlin讲义", "price": 78.9, "publish": "清华书"}
# 使用字典为字符串模板中的key传入值
print(temp % book)
