# Given coin denominations 1, 5, 10, 
# Find the minimum coins needed to make up the value "n"
# By greedy we pick the largest denomination first to minimize the coins

# Uses python3

def get_change(n):
    den = ([10,5,1])
    num_coins = 0
    curr_total = 0
    while (curr_total < n):
        for i in range(0, len(den)):
            if (n - curr_total) >= den[i]:
                curr_total = curr_total + den[i]
                num_coins += 1
                break
    return num_coins

if __name__ == '__main__':
    n = input()
    print(get_change(int(n)))
