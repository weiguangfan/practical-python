# portfolio = [
#     ('GOOG', 100, 490.1),
#     ('IBM', 50, 91.3),
#     ('CAT', 150, 83.44)
# ]
# print(portfolio)
# print(portfolio[0])
# print(portfolio[2])
#########################################
# records = []
# records.append(('GOOG', 100, 490.10))
# records.append(('IBM', 50, 91.3))
# print(records)
#########################################
# records = []
# with open('../Work/Data/portfolio.csv', 'rt') as f:
#     next(f)
#     for line in f:
#         row = line.split(',')
#         records.append((row[0], int(row[1]), float(row[2])))
# print(records)
#########################################
# prices = {
#     'GOOG': 513.25,
#     'CAT': 87.22,
#     'IBM': 93.37,
#     'MSFT': 44.12
# }
# print(prices)
# print(prices['IBM'])
# print(prices['GOOG'])
#########################################
# prices = {}
# prices['GOOG'] = 513.25
# prices['CAT'] = 87.22
# prices['IBM'] = 93.37
# print(prices)
#########################################
# prices = {}
# with open('../Work/Data/prices.csv', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         print(row)
#         prices[row[0]] = float(row[1])
#         # prices[row[0]] = float(row[1].strip('\n'))  # 处理换行符
# print(prices)
#########################################
# prices = {
#     'GOOG': 513.25,
#     'CAT': 87.22,
#     'IBM': 93.37,
#     'MSFT': 44.12
# }
#
# print(prices.get('IBM', 0.0))
# print(prices.get('SCOX', 0.0))
#########################################
# holidays = {
#     (1, 1) : 'New Years',
#     (3, 14) : 'Pi day',
#     (9, 13) : "Programmer's day",
# }
# print(holidays)
# print(holidays[3, 14])
#########################################
# tech_stocks = { 'IBM','AAPL','MSFT' }
# print(tech_stocks)
# tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
# print(tech_stocks)
# print('IBM' in tech_stocks)
# print('FB' in tech_stocks)
# names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
# print(names)
# unique = set(names)
# print(unique)
# unique.add('CAT')
# print(unique)
# unique.remove('YHOO')
# print(unique)
#########################################
s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
