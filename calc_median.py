
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    if N % 2 == 0:
        m1 = int(N/2)
        m2 = int(N/2) + 1
        m1_index = m1 - 1
        m2_index = m2 - 1
        median = (numbers[m1_index] + numbers[m2_index])/2
    else:
        m = int(N+1)/2
        m_index = m - 1
        median = numbers[m_index]
    
    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calculate_median(donations)
    N = len(donations)
    print('Median donation over the last {0} days is {1}'.format(N, median))
