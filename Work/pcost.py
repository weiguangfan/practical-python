# pcost.py
#
# Exercise 1.27
# import csv
#
#
# def portfolio_cost(filename):
#     '''Computes the total cost (shares*price) of a portfolio file'''
#     total_cost = 0.0
#
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#     return total_cost
########################################################


# def portfolio_cost(filename):
#     '''Computes the total cost (shares*price) of a portfolio file'''
#     portfolio = report.read_portfolio(filename)
#     return sum([s['shares'] * s['price'] for s in portfolio])
    # total_cost = 0.0
    #
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         nshares = int(row[1])
    #         price = float(row[2])
    #         total_cost += nshares * price
    # return total_cost


# import sys
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = input('Enter a filename:')
#
# # print(filename)
# # cost = portfolio_cost('../Work/Data/portfolio.csv')
# cost = portfolio_cost(filename)
# print('Total cost:',cost)


########################################################
# import report
#
#
# def portfolio_cost(filename):
#     '''
#     Computes the total cost (shares*price) of a portfolio file
#     '''
#     portfolio = report.read_portfolio(filename)
#     return sum([s.cost() for s in portfolio])
#
#
# def main(args):
#     if len(args) != 2:
#         raise SystemExit('Usage: %s portfoliofile' % args[0])
#     filename = args[1]
#     print('Total cost:', portfolio_cost(filename))
#
#
# if __name__ == '__main__':
#     import sys
#
#     main(sys.argv)
########################################################
import report


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s.cost for s in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))


if __name__ == '__main__':
    import sys

    main(sys.argv)
