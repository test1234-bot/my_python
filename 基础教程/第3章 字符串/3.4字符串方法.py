# center
'''
方法center通过在字符两边添加填充字符(默认空格)使字符串居中
'''
s = '''
The Middle by Jimmy Eat World
'''
print('The Middle by Jimmy Eat World'.center(39))
print('The Middle by Jimmy Eat World'.center(39, '*'))

#find
'''
方法find在字符串中查找子串,找到则返回子串的第一个字符的索引,否则返回-1
'''
s='With a moo-moo here,and a moo-moo there'
print(s.find('moo'))
title="Monty Python's Flying Circus"
print(title.find('Monty'))
print(title.find('Python'))
print(title.find('Flying'))
print(title.find('aaa'))

#join
'''
方法join用于合并序列的元素
'''
seq=['1','2','3','4','5']
sep='+'
print('合并序列：',sep.join(seq))
dirs='','usr','bin','env'
print('/'.join(dirs))