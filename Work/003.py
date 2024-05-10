import os

print(os.getcwd())

# with open('Data/portfolio.csv', 'rt') as f:
#     # data = f.read()
#     # print(data)
#     for line in f:
#         print(line, end='')

# f = open('Data/portfolio.csv', 'rt')
# headers = next(f)
# print(headers)
# for line in f:
#     print(line, end='')
# f.close()


f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
print(headers)
for line in f:
    row = line.split(',')
    print(row)
f.close()




