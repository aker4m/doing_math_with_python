def sum_data(filename):
    s = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            s += float(line.splitlines()[0])
    print('Sum of the numbers: {0}'.format(s))

if __name__ == '__main__':
    sum_data('mydata.txt')
