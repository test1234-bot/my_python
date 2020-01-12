'''
str还提供了如下常用的执行查找、替换等操作的方法
startswith()判断字符串是否以指定子串开头
endswith()判断字符串是否以指定子串结尾
find()查找指定子串在字符串中出现的位置，如果没有找到指定子串，则返回-1
index()查找指定子串在字符串中出现的位置，如果没有找到指定子串，则引发ValueError错误
replace()使用指定子串替换字符串中的目标子串。
translate()使用指定的翻译映射表对字符串执行替换
'''
s='crazyit.org is a good site'
print("判断s是否以crazyit开头:",s.startswith("crazyit"))
print("判断s是否以site结尾:",s.endswith("site"))
print("查找s中'org'出现的位置:",s.find('org'))
print("查找s中'org'出现的位置:",s.index('org'))
# print("从索引9处查找'org'的位置：",s.index('org',9))
print("将字符串中所有的it替换成XXXX:",s.replace('it','XXXX'))
print("将字符串中的1个it替换成XXX:",s.replace('it','XXX',1))
table={97:945,98:946,116:964}
print(s.translate(table))