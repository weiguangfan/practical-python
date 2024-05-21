# from datetime import date
# d = date(2012, 12, 21)
# print(d)
# print(type(d))
# print(str(d))
# print(type(str(d)))
# print(repr(d))
###############################
# import stock
# s = stock.stock('GOOG',100,490.10)
# print(s)
# c = s.cost
# print(c)
# print(c())
# print('Cost: %0.2f' % s.cost())
###############################
# import stock
# goog = stock.stock('GOOG',100,490.1)
# print(goog)
###############################
# import report
# portfolio = report.read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
###############################
# import stock
#
# s = stock.stock('GOOG', 100, 490.1)
# print(s)
# columns = ['name', 'shares']
# for colname in columns:
#     print(colname, '=', getattr(s, colname))
###############################
import report

portfolio = report.read_portfolio('./Data/portfolio.csv')
from tableformat import create_formatter, print_table

formatter = create_formatter('txt')
print_table(portfolio, ['name', 'shares'], formatter)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
