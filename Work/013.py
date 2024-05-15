# a = [1, 2, 3, 4, 5]
# b = [2*x for x in a]
# print(b)
###############################
# names = ['Elwood', 'Jake']
# a = [name.lower() for name in names]
# print(a)
###############################
# a = [1, -5, 4, 2, -2, 10]
# b = [2*x for x in a if x > 0]
# print(b)
###############################
# from report import read_portfolio
# stocks = read_portfolio('../Work/Data/portfolio.csv')
# print(stocks)
# stocknames = [s['name'] for s in stocks]
# print(stocknames)
# a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50]
# print(a)
# cost = sum([s['shares'] * s['price'] for s in stocks])
# print(cost)
###############################
# nums = [1,2,3,4]
# squares = [x * x for x in nums]
# print(squares)
# twice = [2 * x for x in nums if x > 2]
# print(twice)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
# cost = sum([s['shares']*s['price'] for s in portfolio])
# print(cost)
#
# prices = read_prices('../Work/Data/prices.csv')
# print(prices)
# value = sum([s['shares'] * prices[s['name']] for s in portfolio])
# print(value)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print([s['shares'] * s['price'] for s in portfolio])
# print(sum([s['shares'] * s['price'] for s in portfolio]))
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# more100 = [s for s in portfolio if s['shares'] > 100]
# print(more100)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# msftibm = [s for s in portfolio if s['name'] in {'MSFT','IBM'}]
# print(msftibm)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# cost10k = [s for s in portfolio if s['shares'] * s['price'] > 10000]
# print(cost10k)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# name_shares = [(s['name'],s['shares']) for s in portfolio]
# print(name_shares)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# names = {s['name'] for s in portfolio}
# print(names)
###############################
# from report import read_portfolio,read_prices
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# names = {s['name'] for s in portfolio}
# holdings = {name:0 for name in names}
# print(holdings)
###############################
# from report import read_portfolio
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
# holdings = {}
# for s in portfolio:
#     print(s['name'])
#     holdings[s['name']] += s['shares']
# print(holdings)
###############################
# from report import read_portfolio, read_prices
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
# names = {s['name'] for s in portfolio}
# print(names)
# prices = read_prices('../Work/Data/prices.csv')
# print(prices)
# portfolio_prices = {name: prices[name] for name in names}
# print(portfolio_prices)
###############################
import csv

f = open('../Work/Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
select = ['name', 'shares', 'price']
indices = [headers.index(colname) for colname in select]
print(indices)
row = next(rows)
record = {colname: row[index] for colname, index in zip(select, indices)}
print(record)
portfolio = [{colname:row[index] for colname, index in zip(select, indices)}  for row in rows]
print(portfolio)






