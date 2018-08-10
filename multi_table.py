def multi_table(n):
    for i in range(1, 10):
        print('{0} x {1} = {2}'.format(n, i, n*i))

if __name__ == '__main__':
    n = input('Enter a number: ')
    multi_table(int(n))
