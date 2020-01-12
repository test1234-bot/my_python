a=56
print(a)
a=999999999999999999999999999
print(a)
print(type(a))

#以0x或0X开头的整形数值是十六进制形式的整数
hex_value1=0x13
hex_value2=0XaF
print("hex_value1的值为：",hex_value1)
print("hex_value2的值为：",hex_value2)
#以0b或0B开头的整形数值是二进制形式的整数
bin_va1=0B101
print("bin_va1的值为：",bin_va1)
#以0o或0O开头的是八进制形式的整数
oct_va1=0o54
print("oct_vaq的值为：",oct_va1)
oct_va1=0O17
print("oct_vaq的值为：",oct_va1)

#为了提高数值的可读性，Python3.x允许为数值增加下画线为分隔符
one_million=1_000_000
print(one_million)
price=234_234_234
print(price)
adnroid=1234_1234
print(adnroid)
