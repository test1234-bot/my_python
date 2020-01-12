s='crazyit.org is very good'
#获取s中索引2的字符
print(s[2])
#获取s中右边开始，索引为4的字符
print(s[-4])
print("获取字符串s中索引3到索引5(不包含)的子串：",s[3:5])
print("获取字符串s中索引3至倒数5的子串:",s[3:-5])
print("获取字符串s中从倒数6至倒数3的子串:",s[-6:-3])
print("获取字符串中从索引5到结束的子串:",s[5:])
print("获取字符串中从倒数第6个字符至结束的子串:",s[-6:])
#判断s是否包含'very'子串
print("判断s是否包含在'very'子串","very" is s)
print("判断s是否包含在'very'子串","very" in s)
print("输出s的长度:",len(s))
print("输出S字符串最大字符:",max(s))
print("输出s字符串最小字符:",min(s))
