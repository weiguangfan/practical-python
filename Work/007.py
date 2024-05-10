# import csv
# f = open('../Work/Data/portfolio.csv')
# print(f)
# rows = csv.reader(f)
# print(rows)
# headers = next(rows)
# print(headers)
# for row in rows:
#     print(row)
####################################
# import csv
# f = open('../Work/Data/portfolio.csv')
# print(f)
# rows = csv.reader(f)
# print(rows)
# headers = next(rows)
# print(headers)
# row = next(rows)
# print(row)
# cost = row[1] * row[2]
####################################
# import csv
# f = open('../Work/Data/portfolio.csv')
# print(f)
# rows = csv.reader(f)
# print(rows)
# headers = next(rows)
# print(headers)
# row = next(rows)
# print(row)
# t = (row[0], int(row[1]), float(row[2]))
# print(t)
# cost = t[1] * t[2]
# print(cost)
# print(f'{cost:0.2f}')
####################################
# import csv
# f = open('../Work/Data/portfolio.csv')
# print(f)
# rows = csv.reader(f)
# print(rows)
# headers = next(rows)
# print(headers)
# row = next(rows)
# print(row)
# d = {
#     'name': row[0],
#     'shares': int(row[1]),
#     'price': float(row[2])
# }
# print(d)
# cost = d['shares'] * d['price']
# print(cost)
# d['shares'] = 75
# print(d)
# d['date'] = (6, 11, 2007)
# d['account'] = 12345
# print(d)
# print(list(d))
# for k in d:
#     # print('k=',k)
#     print(k, '=', d[k])
# keys = d.keys()
# print(keys)
# del d['account']
# print(keys)
# items = d.items()
# print(items)
# for k, v in d.items():
#     print(k, '=', v)
####################################
list1 = [('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))]
dict1 = dict(list1)
print(dict1)



