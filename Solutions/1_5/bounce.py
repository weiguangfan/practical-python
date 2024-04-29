# bounce.py
# 设置高度变量
height = 100
# 设置弹跳次数变量
bounce = 1
while bounce <= 10:  # 弹跳次数小于等于10
    # 每次弹跳都是上一次的高度的3/5
    height = height * (3/5)
    # 保留小数点后4位
    print(bounce, round(height, 4))
    # 弹跳次数变量自动加1
    bounce += 1
