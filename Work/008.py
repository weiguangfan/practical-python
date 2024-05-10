# def send_email(address, msg):
#     pass
#
#
# email_address = None
# msg = ''
#
# if email_address:
#     send_email(email_address, msg)
################################################
# s = ('GOOG', 100, 490.1)
# print(s)
# s = 'GOOG', 100, 490.1
# print(s)
################################################
# t = ()
# print(t)
# w = ('GOOG',)
# print(w)
################################################
# s = ('GOOG', 100, 490.1)
# print(s)
# name = s[0]
# print(name)
# shares = s[1]
# print(shares)
# price = s[2]
# print(price)
################################################
# s[1] = 75
################################################
# s = (s[0], 75, s[2],)
# print(s)
################################################
# s = ('GOOG', 100, 490.1)
# name, shares, price = s
# print('Cost', shares * price)
################################################
# name, shares = s
################################################
# record = ('GOOG', 100, 490.1)
# print(record)
# symbols = ['GOOG', 'AAPL', 'IBM']
# print(symbols)
################################################
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
print(s)
# print(s['name'], s['shares'])
# print(s['price'])

s['shares'] = 75
s['date'] = '6/6/2007'
print(s)
del s['date']
print(s)
print(s['price'])






