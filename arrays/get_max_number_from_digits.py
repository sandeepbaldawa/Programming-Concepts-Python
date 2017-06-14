'''

Write a function that takes a number as input and outputs the biggest number with the same set of digits.
For example, suppose the input is 423865, then the biggest number with these digits is 865432.

1. Take all digits from the number
2. sort the digits
3. combine and return the result

'''

def get_all_digits(number):
    '''
    Return list of digits from the number
    '''
    #523
    digits = []
    while(number):
        dig = number % 10
        number /= 10
        digits.append(dig)
    return digits

def combine_digits_to_number(number):
    '''
    Return list of digits from the number
    '''
    #523
    base = 0
    res = 0
    #5 * 10^2 + 3 * 10^1 + 2 * 10^0
    for each in digits[::-1]:
        res = res + each * 10**base
        base += 1
    return res


digits = get_all_digits(523)
digits = sorted(digits, reverse=True)
res = combine_digits_to_number(digits)
print res
