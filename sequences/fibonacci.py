# Uses python3
# fib[N] = fib[N-1} + fib[N-2] is v costly in terms of computation
# Below is more efficient approach

def calc_fib(n):
    if (n <= 1):
        return n

    a, b = 0, 1
    while n:
        a, b, n = b, a+b, n-1
    return a

n = int(input())
print(calc_fib(n))
