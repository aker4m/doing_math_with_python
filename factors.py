
def factors(num):
    factors_list = []
    for i in range(1, num+1):
        if num % i == 0:
            factors_list.append(i)
    return factors_list

if __name__ == '__main__':
    num = input('Your Number Please: ')
    num = float(num)
    if num > 0 and num.is_integer():
        result = factors(int(num))
        print(result)
    else:
        print('Please enter a positive integer')

