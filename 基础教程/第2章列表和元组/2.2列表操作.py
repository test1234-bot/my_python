# 索引
greeting = 'Hello'
print(greeting[0])
print(greeting[-1])
print("将以数指定年月日打印出来")
months = [
    'January',
    'February',
    'March',
    'Apirl',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'Novermber',
    'December'
]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

year = input('Year:')
month = input('Month(1-12):')
day = input('Day(1-31):')

month_num = int(month)
day_num = int(day)

month_name = months[month_num - 1]
ordinal = str(day_num) + endings[day_num - 1]

print(month_name + ' ' + ordinal + ',' + year)


