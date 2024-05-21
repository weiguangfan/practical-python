# import foo
#
# print(foo.__dict__)
# print(globals())
#########################
# import stock
# s = stock.stock('GOOG',100,490.1)
# print(s)
# print(s.__dict__)
#########################
# import stock
#
# print(stock.stock.__dict__)
# s = stock.stock('GOOG',100,490.1)
# print(s)
# print(s.__dict__)
# print(s.__class__)
# t = stock.stock('AAPL',50,123.45)
# print(t)
# print(t.__dict__)
# print(t.__class__)
#########################
# import stock
# s = stock.stock('GOOG',100,490.1)
# print(s.__dict__)
# s.shares = 50
# s.date = '6/7/2007'
# print(s.__dict__)
# del s.shares
# print(s.__dict__)
#########################
# import stock
# s = stock.stock('GOOG',100,490.1)
# print(s.__class__)
# print(s.__class__.__dict__)
# print(s.name)
# print(s.cost())
#########################
# import stock
#
# print(stock.MyStock.__bases__)
# print(stock.MyStock.__mro__)
#########################
# class Dog:
#     def noise(self):
#         return 'Bark'
#
#     def chase(self):
#         return 'Chasing!'
#
#
# class Bike:
#     def noise(self):
#         return 'On Your Left'
#
#     def pedal(self):
#         return 'Pedaling!'
#
#
# class Loud:
#     def noise(self):
#         return super().noise().upper()
#
#
# class LoudDog(Loud, Dog):
#     def noise(self):
#         return super().noise().upper()
#
#
# class LoudBike(Loud, Bike):
#     def noise(self):
#         return super().noise().upper()
#########################
# import stock
# goog = stock.stock('GOOG',100,490.10)
# ibm = stock.stock('IBM',50,91.23)
# print(goog)
# print(goog.__dict__)
# print(goog.__class__)
# print(goog.cost())
# print(stock.stock.__dict__['cost'](goog))
# goog.date = '6/11/2007'
# print(goog.__dict__)
# goog.__dict__['time'] = '9:45am'
# print(goog.__dict__)
# print(ibm.__class__)
# print(ibm.cost())
# print(stock.stock.__dict__['cost'](ibm))
# print(goog.time)
# print(ibm)
# print(ibm.__dict__)
# print(stock.stock.__dict__)
# print(stock.stock.__dict__['cost'])
# stock.stock.foo = 42
# print(goog.foo)
# print(ibm.foo)
# print(goog.__dict__)
# print(ibm.__dict__)
# print(stock.stock.__dict__)
#########################
# class Foo(object):
#     a = 13
#
#     def __init__(self, b):
#         self.b = b
#
#
# f = Foo(10)
# g = Foo(20)
# print(f.a)
# print(g.a)
# print(f.b)
# print(g.b)
# Foo.a = 42
# print(f.a)
# print(g.a)
#########################
# import stock
# goog = stock.stock('GOOG',100,490.10)
# s = goog.sell
# print(s)
# print(s.__func__)
# print(stock.stock.__dict__['sell'])
# print(s.__self__)
# # s(25)
# s.__func__(s.__self__,25)
# print(goog.shares)
#########################
import stock


class NewStock(stock.stock):
    def yow(self):
        print('Yow!')


n = NewStock('ACME',50,123.45)
print(n)
print(n.cost())
print(n.yow())
print(NewStock.__bases__)
print(NewStock.__mro__)
for cls in n.__class__.__mro__:
    if 'cost' in cls.__dict__:
        break

print(cls)
print(cls.__dict__['cost'])



