# report.py
#
# Exercise 2.4
# import csv


# def portfolio_cost(filename):
#     total_cost = 0.0
#     with open(filename,'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             print(row)
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#     return total_cost
#####################################################


# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio
#
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
#
# print(portfolio[0])
# print(portfolio[1])
# print(portfolio[1][1])
#####################################################
# total = 0.0
# for s in portfolio:
#     total += s[1] * s[2]
#
# print(total)
#####################################################
# total = 0
# for name, shares, price in portfolio:
#     total += shares * price
# print(total)
#####################################################
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             stock = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio.append(stock)
#     return portfolio
#
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
# print(portfolio[0])
# print(portfolio[1])
# print(portfolio[1]['shares'])
# total = 0.0
# for s in portfolio:
#     total += s['shares'] * s['price']
# print(total)
#####################################################
# from pprint import pprint
# pprint(portfolio)
#####################################################
# prices = {}
# prices['IBM'] = 92.45
# prices['MSFT'] = 45.12
# print(prices)
# print(prices['IBM'])
# print(prices['AAPL'])
# print('AAPL' in prices)
#####################################################
# def read_prices(filename):
#     prices = {}
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 prices[row[0]] = float(row[1])
#             except IndexError:
#                 pass
#     return prices
#
#
# prices = read_prices('../Work/Data/prices.csv')
# print(prices)
# print(prices['IBM'])
# print(prices['MSFT'])
#####################################################
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             stock = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio.append(stock)
#     return portfolio
#
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# print(portfolio)
# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['shares'] * s['price']
# print('Total cost', total_cost)
#
# total_value = 0.0
# for s in portfolio:
#     total_value += s['shares'] * prices[s['name']]
#
# print('Current value', total_value)
# print('Gain', total_value - total_cost)

#####################################################
# import csv
#
# def read_prices(filename):
#     prices = {}
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 prices[row[0]] = float(row[1])
#             except IndexError:
#                 pass
#     return prices
#
#
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             stock = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio.append(stock)
#     return portfolio
#
#
# def make_report(portfolio, prices):
#     rows = []
#     for stock in portfolio:
#         current_price = prices[stock['name']]
#         change = current_price - stock['price']
#         summary = (stock['name'], stock['shares'], current_price, change)
#         rows.append(summary)
#     return rows
#
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# prices = read_prices('../Work/Data/prices.csv')
# report = make_report(portfolio,prices)
# print(report)
# headers = ('Name', 'Shares', 'Price', 'Change',)
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# # for row in report:
# #     print('%10s %10d %10.2f %10.2f' % row)
# # for name, shares, price, change in report:
# #     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
# for name, shares, price, change in report:
#     print(f'{name:>10s} {shares:>10d} {price:$>10,.2f} {change:>10.2f}')

#####################################################
# import csv
# def read_prices(filename):
#     prices = {}
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 prices[row[0]] = float(row[1])
#             except IndexError:
#                 pass
#     return prices
#
#
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=1):
#             record = dict(zip(headers, row))
#             stock = {
#                 'name': record['name'],
#                 'shares': int(record['shares']),
#                 'price': float(record['price'])
#             }
#             portfolio.append(stock)
#     return portfolio
#
#
# def make_report_data(portfolio, prices):
#     rows = []
#     for stock in portfolio:
#         current_price = prices[stock['name']]
#         change = current_price - stock['price']
#         summary = (stock['name'], stock['shares'], current_price, change)
#         rows.append(summary)
#     return rows
#
#
# portfolio = read_portfolio('../Work/Data/portfolio.csv')
# prices = read_prices('../Work/Data/prices.csv')
# report = make_report_data(portfolio, prices)
# print(report)
# headers = ('Name', 'Shares', 'Price', 'Change',)
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# # for row in report:
# #     print('%10s %10d %10.2f %10.2f' % row)
#
# # for name, shares, price, change in report:
# #     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
#
# for name, shares, price, change in report:
#     print(f'{name:>10s} {shares:>10d} {price:$>10,.2f} {change:>10.2f}')
#####################################################
# import csv
#
#
# def read_prices(filename):
#     prices = {}
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 prices[row[0]] = float(row[1])
#             except IndexError:
#                 pass
#     return prices
#
#
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=1):
#             record = dict(zip(headers, row))
#             stock = {
#                 'name': record['name'],
#                 'shares': int(record['shares']),
#                 'price': float(record['price'])
#             }
#             portfolio.append(stock)
#     return portfolio
#
#
# def make_report_data(portfolio, prices):
#     rows = []
#     for stock in portfolio:
#         current_price = prices[stock['name']]
#         change = current_price - stock['price']
#         summary = (stock['name'], stock['shares'], current_price, change)
#         rows.append(summary)
#     return rows
#
#
# def print_report(reportdata):
#     headers = ('Name', 'Shares', 'Price', 'Change',)
#     print('%10s %10s %10s %10s' % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for row in reportdata:
#         print('%10s %10d %10.2f %10.2f' % row)
#
#
# def portfolio_report(portfoliofile, pricefile):
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)
#     report = make_report_data(portfolio, prices)
#     print_report(report)
#
#
# # print(portfolio_report('../Work/Data/portfolio.csv', '../Work/Data/prices.csv'))
#####################################################
# import csv
# import fileparse
#
# def read_prices(filename):
#     '''
#     Read a CSV file of price data into a dict mapping names to prices.
#     '''
#     return dict(fileparse.parse_csv(filename,types=[str,float],has_headers=False))
#     # prices = {}
#     # with open(filename, 'rt') as f:
#     #     rows = csv.reader(f)
#     #     for row in rows:
#     #         try:
#     #             prices[row[0]] = float(row[1])
#     #         except IndexError:
#     #             pass
#     # return prices
#
#
# def read_portfolio(filename):
#     '''
#     Read a stock portfolio file into a list of dictionaries with keys
#     name, shares, and price.
#     '''
#     return fileparse.parse_csv(filename, select=['name','shares','price'],types=[str,int,float])
#     # portfolio = []
#     # with open(filename, 'rt') as f:
#     #     rows = csv.reader(f)
#     #     headers = next(rows)
#     #     for rowno, row in enumerate(rows, start=1):
#     #         record = dict(zip(headers, row))
#     #         stock = {
#     #             'name': record['name'],
#     #             'shares': int(record['shares']),
#     #             'price': float(record['price'])
#     #         }
#     #         portfolio.append(stock)
#     # return portfolio
#
#
# def make_report_data(portfolio, prices):
#     '''
#     Make a list of (name,shares,price,change) tuples given a portfolio list and prices dictionary.
#     '''
#     rows = []
#     for stock in portfolio:
#         current_price = prices[stock['name']]
#         change = current_price - stock['price']
#         summary = (stock['name'], stock['shares'], current_price, change)
#         rows.append(summary)
#     return rows
#
#
# def print_report(reportdata):
#     '''
#     Print a nicely formated table from a list of (name,shares,price,change) tuples.
#     '''
#     headers = ('Name', 'Shares', 'Price', 'Change',)
#     print('%10s %10s %10s %10s' % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for row in reportdata:
#         print('%10s %10d %10.2f %10.2f' % row)
#
#
# def portfolio_report(portfoliofile, pricefile):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)
#     report = make_report_data(portfolio, prices)
#     print_report(report)
#
# # portfolio_report('../Work/Data/portfolio.csv','../Work/Data/prices.csv')
#####################################################
# import fileparse
#
#
# def read_prices(filename):
#     '''
#     Read a CSV file of price data into a dict mapping names to prices.
#     '''
#     return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))
#
#
# def read_portfolio(filename):
#     '''
#     Read a stock portfolio file into a list of dictionaries with keys
#     name, shares, and price.
#     '''
#     return fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])
#
#
# def make_report_data(portfolio, prices):
#     '''
#     Make a list of (name,shares,price,change) tuples given a portfolio list and prices dictionary.
#     '''
#     rows = []
#     for stock in portfolio:
#         current_price = prices[stock['name']]
#         change = current_price - stock['price']
#         summary = (stock['name'], stock['shares'], current_price, change)
#         rows.append(summary)
#     return rows
#
#
# def print_report(reportdata):
#     '''
#     Print a nicely formated table from a list of (name,shares,price,change) tuples.
#     '''
#     headers = ('Name', 'Shares', 'Price', 'Change',)
#     print('%10s %10s %10s %10s' % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for row in reportdata:
#         print('%10s %10d %10.2f %10.2f' % row)
#
#
# def portfolio_report(portfoliofile, pricefile):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)
#     report = make_report_data(portfolio, prices)
#     print_report(report)
#
#
# def main(args):
#     if len(args) != 3:
#         raise SystemExit('Usage:%s portfile pricefile' % args[0])
#     portfolio_report(args[1], args[2])
#
#
# if __name__ == '__main__':
#     import sys
#     main(sys.argv)


#####################################################
import fileparse


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])


def make_report_data(portfolio, prices):
    '''
    Make a list of (name,shares,price,change) tuples given a portfolio list and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name,shares,price,change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change',)
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report = make_report_data(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit('Usage:%s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)

