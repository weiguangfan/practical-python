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
class stock:
    '''
    An instance of a stock holding consisting of name,shares,and price.
    '''

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

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
class MyStock(stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to 'super' and '__init__'
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()


s = MyStock('GOOG', 100, 490.1, 1.25)
print(s.cost())
print(isinstance(s, stock))
##########################################





















