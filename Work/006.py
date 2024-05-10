with open('../Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    print(headers.split(','))
    for line in f:
        fields = line.split(',')
        try:
            shares = int(fields[1])
            print(shares)
        except ValueError:
            print("Couldn't parse", line)
