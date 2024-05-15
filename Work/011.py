# a = 'Hello'
# b = [1, 4, 5]
# c = ('GOOG', 100, 490.1)
# print(a[0])
# print(b[-1])
# print(c[1])
# print(len(a))
# print(len(b))
# print(len(c))
################################
# a = 'Hello'
# b = [1, 4, 5]
# print(a * 3)
# print(b * 2)
################################
# a = (1, 2, 3)
# b = (4, 5)
# print(a + b)
# c = [1, 5]
# print(a + c)  # 报错
################################
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(a[2:5])
# print(a[-5])
# print(a[:3])
################################
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(a)
# a[2:4] = [10, 11, 12]
# print(a)
################################
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(a)
# del a[2:4]
# print(a)
################################
# s = [1, 2, 3, 4]
# print(sum(s))
# print(min(s))
# print(max(s))
# t = ['Hello', 'World']
# print(max(t))
################################
# s = [1, 4, 9, 16]
# for i in s:
#     print(i)
################################
# for i in range(100):
#     print(i)
################################
# for j in range(10,20):
#     print(j)
################################
# for k in range(10, 50, 2):
#     print(k)
################################
# names = ['Elwood', 'Jake', 'Curtis']
# for i, name in enumerate(names):
#     print(i, name)
################################
# with open('../Work/Data/prices.csv') as f:
#     for lineno, line in enumerate(f, start=1):
#         print(lineno, line)
################################
# points = [
#     (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
# ]
#
# print(points)
# for x,y in points:
#     print(x,y)
################################
# columns = ['name', 'shares', 'price']
# values = ['GOOG', 100, 490.1 ]
# pairs = zip(columns,values)
# print(pairs)
# for column, value in pairs:
#     print(column,value)
################################
# columns = ['name', 'shares', 'price']
# values = ['GOOG', 100, 490.1 ]
# pairs = zip(columns,values)
# d = dict(pairs)
# print(d)
################################
# for n in range(10):
#     print(n, end=' ')
################################
# for n in range(10, 0, -1):
#     print(n, end=' ')
################################
# for n in range(0, 10, 2):
#     print(n, end=' ')
################################
# data = [4, 9, 1, 25, 16, 100, 49]
# print(min(data))
# print(max(data))
# print(sum(data))
# for x in data:
#     print(x)
# for n, x in enumerate(data):
#     print(n, x)
################################
# data = [4, 9, 1, 25, 16, 100, 49]
# for n in range(len(data)):
#     print(data[n])
################################
# import csv
# f = open('../Work/Data/portfolio.csv')
# rows = csv.reader(f)
# headers = next(rows)
# print(headers)
# row = next(rows)
# print(row)
# print(zip(headers, row))
# print(list(zip(headers, row)))
# record = dict(zip(headers, row))
# print(record)
################################
# prices = {
#     'GOOG' : 490.1,
#     'AA' : 23.45,
#     'IBM' : 91.1,
#     'MSFT' : 34.23
# }
#
# print(prices.items())
#
# pricelist = list(zip(prices.values(),prices.keys()))
# print(pricelist)
# print(min(pricelist))
# print(max(pricelist))
# print(sorted(pricelist))
################################
# a = [1, 2, 3, 4]
# b = ['w', 'x', 'y', 'z']
# c = [0.2, 0.4, 0.6, 0.8]
# print(list(zip(a, b, c)))
################################
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a, b)))





