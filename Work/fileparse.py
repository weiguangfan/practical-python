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
# import csv
#
#
# def parse_csv(filename, select=None):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         if select:
#             indices = [headers.index(colname) for colname in select]
#             headers = select
#         else:
#             indices = []
#
#         records = []
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[index] for index in indices]
#
#             record = dict(zip(headers, row))
#             records.append(record)
#
#     return records
#
#
# select = ['name', 'shares']
# portfolio = parse_csv('../Work/Data/portfolio.csv', select)
# print(portfolio)
######################################################
# import csv
#
#
# def parse_csv(filename, select=None, types=None):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         if select:
#             indices = [headers.index(colname) for colname in select]
#             headers = select
#         else:
#             indices = []
#
#         records = []
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[index] for index in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             record = dict(zip(headers, row))
#             records.append(record)
#
#     return records
######################################################
#
#
# def parse_csv(filename, select=None, types=None, has_headers=True):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows) if has_headers else []
#         if select:
#             indices = [headers.index(colname) for colname in select]
#             headers = select
#         else:
#             indices = []
#
#         records = []
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[index] for index in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             if headers:
#                 record = dict(zip(headers, row))
#             else:
#                 record = tuple(row)
#             records.append(record)
#
#     return records
#

######################################################
# import csv
#
#
# def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f, delimiter=delimiter)
#         headers = next(rows) if has_headers else []
#         if select:
#             indices = [headers.index(colname) for colname in select]
#             headers = select
#         else:
#             indices = []
#
#         records = []
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[index] for index in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             if headers:
#                 record = dict(zip(headers, row))
#             else:
#                 record = tuple(row)
#             records.append(record)
#
#     return records
#
# portfolio = parse_csv('../Work/Data/portfolio.dat', types=[str,int,float],delimiter=' ')
# print(portfolio)
######################################################
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


# portfolio = parse_csv('../Work/Data/prices.csv', select=['name', 'price'], has_headers=False)
# portfolio = parse_csv('../Work/Data/missing.csv', types=[str, int, float])
# print(portfolio)
