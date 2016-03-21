def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    a, b = 0, 1
    while n:
        a, b, n = b, (a+b), n-1
        a, b = a%10, b%10
    return a

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
