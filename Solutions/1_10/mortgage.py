# mortgage.py
# 贷款总金额变量
principal = 500000.0
# 固定利率变量
rate = 0.05
# 每月支付金额变量
payment = 2684.11
# 已支付总金额变量
total_paid = 0.0
# 还款月数变量
month = 0
# 假如：前12个月，每月额外支出金额
# 假如：连续还款5年后，接下来的4年每个月额外多还款1000美元
extra_payment = 1000.0  # 额外还款金额
extra_payment_start_month = 61  # 连续5年后，接下来的4年的开始月数
extra_payment_end_month = 108  # 持续4年的结束月数

while principal > 0:  # 只要贷款总金额大于零
    month = month + 1  # 月数自动加1
    principal = principal * (1+rate/12) - payment  # 乘以利率后的总贷款金额，减去每月支付金额，等于剩余的贷款金额
    total_paid = total_paid + payment  # 总还款，等于之前的已支付的总金额，加上本月支付金额

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

        print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)




