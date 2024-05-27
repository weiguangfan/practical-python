# follow.py
# import os
# import time
#
# f = open('./Data/stocklog.csv')
# # Move file pointer 0 bytes from end of file
# f.seek(0, os.SEEK_END)
#
# while True:
#     line = f.readline()
#     if line == '':
#         # Sleep briefly and retry
#         time.sleep(0.1)
#         continue
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s} {price:>10.2f} {change:>10.2f} ')
############################################
import os
import time


def follow(filename):
    '''
    Generator that produce a sequence of lines
    being written at the end of a file
    '''
    f = open('./Data/stocklog.csv')
    # Move file pointer 0 bytes from end of file
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            # Sleep briefly and retry
            time.sleep(0.1)
            continue
        yield line


# Example use
if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('./Data/portfolio.csv')
    for line in follow('./Data/stocklog.csv'):
        row = line.strip(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f} ')













