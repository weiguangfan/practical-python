# portfolio = [
#     ('GOOG', 100, 490.1),
#     ('IBM', 50, 91.1),
#     ('CAT', 150, 83.44),
#     ('IBM', 100, 45.23),
#     ('GOOG', 75, 572.45),
#     ('AA', 50, 23.15)
# ]

# from collections import Counter
#
# total_shares = Counter()
# print(total_shares)
# for name, shares, price in portfolio:
#     total_shares[name] += shares
# print(total_shares)
# print(total_shares['IBM'])
##############################################
# portfolio = [
#     ('GOOG', 100, 490.1),
#     ('IBM', 50, 91.1),
#     ('CAT', 150, 83.44),
#     ('IBM', 100, 45.23),
#     ('GOOG', 75, 572.45),
#     ('AA', 50, 23.15)
# ]
# from collections import defaultdict
#
# holdings = defaultdict(list)
# print(holdings)
# for name, shares, price in portfolio:
#     holdings[name].append((shares, price))
# print(holdings)
# print(holdings['IBM'])
##############################################
# from collections import deque
#
# history = deque(maxlen=2)
# print(history)
# with open('../Work/Data/prices.csv', 'rt') as f:
#     for line in f:
#         history.append(line)
# print(history)
##############################################
from report import read_portfolio
from collections import Counter
portfolio = read_portfolio('../Work/Data/portfolio.csv')
holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']
print(holdings)
print(holdings['IBM'])
print(holdings['MSFT'])
print(holdings.most_common(3))

portfolio2 = read_portfolio('../Work/Data/portfolio2.csv')
print(portfolio2)
holdings2 = Counter()
for s in portfolio2:
    holdings2[s['name']] += s['shares']
print(holdings2)

combined = holdings + holdings2
print(combined)









