# fileparse.py
#
# Exercise 3.3
# import csv
#
#
# def parse_csv(filename):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         records = []
#         for row in rows:
#             if not row:
#                 continue
#             record = dict(zip(headers, row))
#             records.append(record)
#
#     return records
#
#
# portfolio = parse_csv('../Work/Data/portfolio.csv')
# print(portfolio)
######################################################
import csv


def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]

            record = dict(zip(headers, row))
            records.append(record)

    return records

select = ['name', 'shares']
portfolio = parse_csv('../Work/Data/portfolio.csv',select)
print(portfolio)
