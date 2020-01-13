def divide(num):
    integer = int(num)
    fractiion = round((num - integer) * 100)
    return (str(integer), str(fractiion))


han_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit_list = ['十', '佰', '千']


def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    for i in range(num_len):
        num = int(num_str[i])
        if i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        else:
            result += han_list[num]
    return result


def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print("数字太大了")
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + "亿" + four_to_hanstr(num_str[-8:-4]) + "万" + four_to_hanstr(num_str[-4:])
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4]) + "万" + four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)


def fraction_to_str(num_str):
    result = ""
    str_len = len(num_str)
    for i in range(str_len):
        num = num_str[i]
        if num != 0 and i != str_len - 1:
            result += han_list[num] + "角"
        else:
            result += han_list[num]


num = float(input("请输入浮点数:"))
integer, fraction = divide(num)
print(integer_to_str(integer))
print(fraction)

print(fraction_to_str(fraction))
