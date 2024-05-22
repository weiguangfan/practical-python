# class Person(object):
#     def __init__(self, name):
#         self._name = name
#
#
# p = Person('Guido')
# print(p)
# print(p._name)
# p._name = 'Dave'
# print(p._name)
#################################
# import stock
# s = stock.stock('IBM',50,91.1)
# print(s.__dict__)
# s.shares = 100
# print(s.shares)
# print(s.__dict__)
# s.shares = 'hundred'
# print(s.shares)
# print(s.__dict__)
# s.shares = [1,0,0]
# print(s.shares)
# print(s.__dict__)
#################################
import stock
s = stock.stock('IBM',50,91.1)
print(s.shares)
s.shares = 75
print(s.shares)
print(s.cost)
s.price = 385.15
# s.prices = 410.2  # 报错
# print(s.__dict__)  # 报错








