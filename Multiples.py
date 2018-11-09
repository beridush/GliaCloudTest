MAX = 1000
n1, n2 = 3, 5

def sum_of_arithmetic_series_from_1(n):
    return (n + 1) * n / 2

def main():
    # print(sum_of_arithmetic_series_from_1(5))
    print(n1 * sum_of_arithmetic_series_from_1((MAX - 1) // n1) +
          n2 * sum_of_arithmetic_series_from_1((MAX - 1) // n2) -
          n1 * n2 * sum_of_arithmetic_series_from_1((MAX - 1) // (n1 * n2)))

if __name__ == '__main__':
    main()