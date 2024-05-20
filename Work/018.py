# nums = [1,2,3]
# print(nums)
# nums.append(4)
# print(nums)
# nums.insert(1,10)
# print(nums)
###########################
# class Player(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def left(self, amt):
#         self.move(-amt, 0)
#
#     def damage(self, pts):
#         self.health -= pts
#
#
# print(Player)
#
# a = Player(2, 3)
# print(a)
# b = Player(10, 20)
# print(b)
#
# print(a.x)
# print(b.x)
# print(a.move(1, 2))
###########################
# import stock
# a = stock.stock('GOOG',100,490.10)
# print(a)
# print(a.name)
# print(a.shares)
# print(a.price)
# b = stock.stock('AAPL',50,122.34)
# c = stock.stock('IBM',75,91.75)
# print(b.shares * b.price)
# print(c.shares * c.price)
# stocks = [a,b,c]
# print(stocks)
# for s in stocks:
#     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f} ')
###########################
# import stock
#
# s = stock.stock('GOOG', 100, 490.10)
# print(s.cost())
# print(s.shares)
# print(s.sell(25))
# print(s.shares)
# print(s.cost())
###########################
# import fileparse
# import stock
# with open('../Work/Data/portfolio.csv') as lines:
#     portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
# portfolio = [stock.stock(d['name'],d['shares'],d['price']) for d in portdicts]
# print(portfolio)
# print(sum([s.cost() for s in portfolio]))
###########################
import pcost

print(pcost.portfolio_cost('../Work/Data/portfolio.csv'))

import report

print(report.portfolio_report('../Work/Data/portfolio.csv', '../Work/Data/prices.csv'))



