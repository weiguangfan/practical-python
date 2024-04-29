# sears.py
# 一枚纸币的厚度变量，单位转换，毫米转换成米
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
# 初始大厦高度变量
sears_height = 442 # Height (meters)
# 纸币数量的变量
num_bills = 1
# 天数的变量
day = 1

while num_bills * bill_thickness < sears_height:  # 纸币的总高度低于大厦的高度
    print(day, num_bills, num_bills * bill_thickness)  # 打印哪天、多少纸币、纸币总高度
    day = day + 1  # 天数自动加1
    # day = days + 1  # 故意制造一个错误
    num_bills = num_bills * 2  # 纸币数量自动翻倍

# 循环停止后打印，天数、总纸币数、纸币总高度
print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)