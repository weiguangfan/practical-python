# name = 'IBM'
# shares = 100
# price = 91.1
# print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
#####################################################
# s = {
#     "name": 'IBM',
#     "shares": 100,
#     "price": 91.1
# }
# print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(s))
#####################################################
# print('{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1))
# print('{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1))
#####################################################
# print(('The value is %d' % 3))
# print(('%5d %-5d %10d' % (3, 4, 5)))
# print(('%0.2f' % (3.1415926,)))
#####################################################
# print(b'%s has %d messages' % (b'Dave', 37))
# print(b'%b has %d messages' % (b'Dave', 37))
#####################################################
# value = 42863.1
# print(value)
# print(f'{value:0.4f}')
# print(f'{value:>16.2f}')
# print(f'{value:<16.2f}')
# print(f'{value:*>16,.2f}')
#####################################################
# value = 42863.1
# print('%0.4f' % value)
# print('%16.2f' % value)
#####################################################
value = 42863.1
f = '%0.4f' % value
print(f)



