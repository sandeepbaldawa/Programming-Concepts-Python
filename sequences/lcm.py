# Uses python3

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    l = (a*b)//gcd(a,b)
    return l

if __name__ == '__main__':
    n = input()
    a, b = map(int, n.split())
    print(lcm(a, b))
