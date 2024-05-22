# a = 'hello'
# for c in a:
#     print(c)
#################
# b = {'name':'Dave','password':'foo'}
# for k in b:
#     print(k)
#################
# c = [1,2,3,4]
# for i in c:
#     print(i)
#################
# f = open('./foo')
# for x in f:
#     print(x)
#################
# f = open('./foo')
# _iter = f.__iter__()
# print(_iter)
# while True:
#     try:
#         x = _iter.__next__()
#         print(x)
#     except StopIteration:
#         break
#################
# x = [1,2,3]
# it = x.__iter__()
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# # print(it.__next__())  # 没有元素就会报错
#################
# f = open('./Data/portfolio.csv')
# print(f.__iter__())
# print(next(f))
# print(next(f))
# print(next(f))
#################
# import report
# a = report.read_portfolio('./Data/portfolio.csv')
# print(a)
# for s in a:
#     print(s)
#################
# import report
# a = report.portfolio_report('./Data/portfolio.csv','./Data/prices.csv')
# print(a)
#################
# import pcost
#
# print(pcost.portfolio_cost('./Data/portfolio.csv'))
#################
import report
portfolio = report.read_portfolio('./Data/portfolio.csv')
print(portfolio)
print(len(portfolio))
print(portfolio[0])
print(portfolio[1])
print(portfolio[0:3])
print('IBM' in portfolio)
print('AAPL' in portfolio)
















