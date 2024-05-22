# class stock:
#     '''
#     An instance of a stock holding consisting of name,shares,and price.
#     '''
#
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
#     def cost(self):
#         '''
#         Return the cost as shares*price
#         '''
#         return self.shares * self.price
#
#     def sell(self, nshares):
#         '''
#         Sell a number of shares
#         '''
#         self.shares -= nshares

##########################################
# class stock:
#     '''
#     An instance of a stock holding consisting of name,shares,and price.
#     '''
#
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
#     def cost(self):
#         '''
#         Return the cost as shares*price
#         '''
#         return self.shares * self.price
#
#     def sell(self, nshares):
#         '''
#         Sell a number of shares
#         '''
#         self.shares -= nshares


# class MyStock(stock):
#     def panic(self):
#         self.sell(self.shares)

##########################################
# s = MyStock('GOOG', 100, 490.1)
# print(s)
# print(s.shares)
# s.sell(25)
# print(s.shares)
# s.panic()
# print(s.shares)
##########################################
# class MyStock(stock):
#     def panic(self):
#         self.sell(self.shares)
#
#     def cost(self):
#         return 1.25 * self.shares * self.price
#
#
# s = MyStock('GOOG',100,490.1)
# print(s.cost())
##########################################
# class MyStock(stock):
#     def panic(self):
#         self.sell(self.shares)
#
#     def cost(self):
#         # Check the call to 'super'
#         actual_cost = super().cost()
#         return 1.25 * actual_cost
#
#
# s = MyStock('GOOG', 100, 490.1)
# print(s.cost())
##########################################
# class MyStock(stock):
#     def __init__(self, name, shares, price, factor):
#         # Check the call to 'super' and '__init__'
#         super().__init__(name, shares, price)
#         self.factor = factor
#
#     def panic(self):
#         self.sell(self.shares)
#
#     def cost(self):
#         return self.factor * super().cost()


# s = MyStock('GOOG', 100, 490.1, 1.25)
# print(s.cost())
# print(isinstance(s, stock))
##########################################
# class stock:
#     '''
#     An instance of a stock holding consisting of name,shares,and price.
#     '''
#
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
#     def __repr__(self):
#         return f'Stock({self.name!r},{self.shares!r},{self.price!r})'
#
#     def cost(self):
#         '''
#         Return the cost as shares*price
#         '''
#         return self.shares * self.price
#
#     def sell(self, nshares):
#         '''
#         Sell a number of shares
#         '''
#         self.shares -= nshares
#
#
# class MyStock(stock):
#     def __init__(self, name, shares, price, factor):
#         # Check the call to 'super' and '__init__'
#         super().__init__(name, shares, price)
#         self.factor = factor
#
#     def panic(self):
#         self.sell(self.shares)
#
#     def cost(self):
#         return self.factor * super().cost()
#

##########################################
# class stock:
#     '''
#     An instance of a stock holding consisting of name,shares,and price.
#     '''
#
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.set_shares(shares)
#         self.price = price
#
#     def __repr__(self):
#         return f'Stock({self.name!r},{self.shares!r},{self.price!r})'
#
#     def get_shares(self):
#         return self.shares
#
#     def set_shares(self, value):
#         if not isinstance(value, int):
#             raise TypeError('Expected an int')
#         self._shares = value
#
#     def cost(self):
#         '''
#         Return the cost as shares*price
#         '''
#         return self.shares * self.price
#
#     def sell(self, nshares):
#         '''
#         Sell a number of shares
#         '''
#         self.shares -= nshares

##########################################
class stock:
    '''
    An instance of a stock holding consisting of name,shares,and price.
    '''
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def __repr__(self):
        return f'Stock({self.name!r},{self.shares!r},{self.price!r})'

    @property
    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares
