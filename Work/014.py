# a = [1, 2, 3]
# # print(a)
# print(id(a))
# b = a
# # print(b)
# print(id(b))
# c = [a, b]
# # print(c)
# print(id(c))
###################################
# a.append(999)
# print(a)
# print(id(a))
# print(b)
# print(id(b))
# print(c)
# print(id(c))
###################################
# a = [1,2,3]
# print(a)
# print(id(a))
# b = a
# print(b)
# print(id(b))
# a = [4,5,6]
# print(a)
# print(id(a))
###################################
# a = [1,2,3]
# b = a
# print(a is b)
# print(id(a))
# print(id(b))
###################################
# a = [1,2,3]
# b = a
# c = [1,2,3]
# print(a is b)
# print(a is c)
# print(a == c)
###################################
# a = [2,3,[100,101],4]
# print(a)
# print(id(a))
# b = list(a)
# print(b)
# print(id(b))
# print(a is b)
###################################
# a[2].append(102)
# print(a)
# print(id(a))
# print(b)
# print(b[2])
# print(id(b))
# print(a[2] is b[2])
###################################
# a = [2,3,[100,101],4]
# print(a)
# print(id(a))
# import copy
# b = copy.deepcopy(a)
# print(b)
# print(id(b))
# a[2].append(102)
# print(a)
# print(id(a))
# print(b)
# print(b[2])
# print(id(b))
# print(a[2] is b[2])
###################################
# a = 42
# b = 'Hello World'
# print(type(a))
# print(type(b))
# if isinstance(a,list):
#     print('a is a list')
# if isinstance(a,(list,tuple)):
#     print('a is a list or tupel')
###################################
# import math
# items = [abs,math,ValueError]
# print(items)
# print(items[0](-45))
# print(items[1].sqrt(2))
# try:
#     x = int('not a number')
# except items[2]:
#     print('Failed!')
###################################
# types = [str,int,float]
# import csv
# f = open('../Work/Data/portfolio.csv')
# rows = csv.reader(f)
# headers = next(rows)
# row = next(rows)
# print(row)
# # print(row[1] * row[2])
# print(types[1])
# print(row[1])
# print(types[1](row[1]))
# print(types[2](row[2]))
# print(types[1](row[1]) * types[2](row[2]))
# r = list(zip(types,row))
# print(r)
#
# converted = []
# for func,val in zip(types,row):
#     converted.append(func(val))
# print(converted)
# print(converted[1] * converted[2])
# converted2 = [func(val) for func,val in zip(types,row)]
# print(converted2)
#
# print(dict(zip(headers, converted)))
# print({name: func(val) for name, func, val in zip(headers, types, row)})

###################################
import csv
f = open('../Work/Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(headers)
print(row)
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func,val in zip(types,row)]
record = dict(zip(headers,converted))
print(record)
print(record['name'])
print(record['price'])











###################################















