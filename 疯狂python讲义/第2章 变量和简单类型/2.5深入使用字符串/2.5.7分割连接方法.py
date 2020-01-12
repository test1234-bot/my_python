'''
split()将字符串按照指定分割符分割成多少个短语
join()将多个短语连接成字符串
'''

s = 'crazyit.org is a good site'
print("使用空白对字符串进行分割:", s.split())
print("使用空白字符进行分隔，并最多分隔前两个单词:", s.split(None, 2))

print("使用/作为分隔符，将s字符串连接起来:","/".join(s.split()))
print("使用,作为分隔符，将s字符串连接起来:",",".join(s.split()))
