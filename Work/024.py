def countdown(n):
    # Added a print statement
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


##################################
# for x in countdown(10):
#     print(x, end=' ')
##################################
# x = countdown(10)
# There is NO PRINT STATEMENT
# x is a generator object
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())  # error
##################################
def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line


##################################
# for line in open('../Work/Data/portfolio.csv'):
#     print(line, end='')
##################################
for line in filematch('./Data/portfolio.csv', 'IBM'):
    print(line, end='')
##################################



















