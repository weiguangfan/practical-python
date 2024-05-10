# pcost.py

# total_cost = 0.0
#
# with open('../../Work/Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     print(headers)
#     for line in f:
#         row = line.split(',')  # 获取每一行，分割后是一个列表
#         nshares = int(row[1])  # 获取股份数量
#         price = float(row[2])  # 获取股份的购买价格
#         total_cost += nshares * price  # 累计计算每支股票的价值，得到该投资组合的总价值
#
# print('Total cost', total_cost)

#################################################################
# def portfolio_cost(filename):
#     total_cost = 0.0
#     with open(filename, 'rt') as f:
#         headers = next(f)
#         print(headers)
#         for line in f:
#             row = line.split(',')  # 获取每一行，分割后是一个列表
#             # 跳过为空的数据
#             # if (row[1] is not True) or (row[2] is not True):
#             #     continue
#             nshares = int(row[1])  # 获取股份数量
#             price = float(row[2])  # 获取股份的购买价格
#             total_cost += nshares * price  # 累计计算每支股票的价值，得到该投资组合的总价值
#     return total_cost
#
#
# # cost = portfolio_cost('../../Work/Data/portfolio.csv')
# # print('Total cost:', cost)
#
# print(portfolio_cost('../../Work/Data/missing.csv'))
#################################################################
# import csv
#
#
# def portfolio_cost(filename):
#     total_cost = 0.0
#     with open(filename,'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         print(headers)
#         for row in rows:
#             print(row)
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#         return total_cost
# print(portfolio_cost('../../Work/Data/portfolio.csv'))
#################################################################
import sys, csv


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        for row in rows:
            print(row)
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost


print(sys.argv)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../../Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
