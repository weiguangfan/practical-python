# def add(x, y):
#     return x + y
#
#
# print(add(3, 4))
# print(add('Hello', 'World'))
# print(add('3', '4'))
#
# # print(add(3, '4'))  # 报错
#########################################
# import math as m
#
#
# def rectangular(r, theta):
#     x = r * m.cos(theta)
#     y = r * m.sin(theta)
#     return x, y
#########################################
# from math import sin, cos
#
#
# def rectangular(r, theta):
#     x = r * cos(theta)
#     y = r * sin(theta)
#     return x, y
#########################################
# import math
# # vs
# import math as m
# # vs
# from math import sin,cos
#########################################
# import sys
#
# print(sys.modules.keys())
#########################################
# import sys
#
# print(sys.path)
#########################################
# import sys
#
# sys.path.append('')  # 添加路径
#########################################
# import fileparse
#
# help(fileparse)
# print(dir(fileparse))
#########################################
# import fileparse
#
# portfolio = fileparse.parse_csv('../Work/Data/portfolio.csv', select=['name', 'shares', 'price'],
#                                 types=[str, int, float])
# print(portfolio)
# pricelist = fileparse.parse_csv('../Work/Data/prices.csv', types=[str, float], has_headers=False)
# print(pricelist)
# prices = dict(pricelist)
# print(prices)
# print(prices['IBM'])
#########################################
from fileparse import parse_csv

portfolio = parse_csv('../Work/Data/portfolio.csv', select=['name', 'shares', 'price'],types=[str, int, float])
print(portfolio)


















