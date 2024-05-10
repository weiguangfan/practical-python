with open('foo','rt') as file:
    print(file.read())

with open('bar', 'rt') as file2:
    # print(file2.read())
    for line in file2:
        print(line)
with open('foo', 'wt') as out:
    # out.write('hello world\n')
    print('hello world', file=out)