# # Provide a filename
# def read_data(filename):
#     records = []
#     with open(filename) as f:
#         for line in f:
#             pass
#             records.append(line)
#     return records
#
#
# d = read_data('file.csv')
#

####################################
# # Provide lines
#
# def read_data(lines):
#     records = []
#     for line in lines:
#         pass
#         records.append(r)
#     return records
#
#
# with open('file.csv') as f:
#     d = read_data(f)
#
# # A CSV file
# lines = open('data.csv')
# data = read_data(lines)
#
# # A zipped file
# import gzip
# lines = gzip.open('data.csv.gz','rt')
# data = read_data(lines)
#
# # The Standard Input
# import sys
# lines = sys.stdin
# data = read_data(lines)
#
# # A list of strings
# lines = ['ACME,50,91.1','IBM,75,123.45']
# data = read_data(lines)
####################################
# import fileparse
# portfolio = fileparse.parse_csv('../Work/Data/portfolio.csv',types=[str,int,float])
# print(portfolio)
####################################
# import fileparse
# import gzip
# with gzip.open('../Work/Data/portfolio.csv.gz','rt') as file:
#     port = fileparse.parse_csv(file,types=[str,int,float])
#     print(port)
#
# lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
# port = fileparse.parse_csv(lines,types=[str,int,float])
# print(port)

####################################
import fileparse
port = fileparse.parse_csv('../Work/Data/portfolio.csv', types=[str,int,float])
print(port)  # 输入文件名就不行了
####################################










