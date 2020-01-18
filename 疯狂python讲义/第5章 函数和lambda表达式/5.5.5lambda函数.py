# 使用内置map()函数
x = map(lambda x: x * x, range(8))
print([e for e in x])

x=map(lambda x:x*x if x%2==0 else 0,range(8))
print([e for e in x])
