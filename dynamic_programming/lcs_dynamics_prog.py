def lcs_helper_dynamic(X, Y, m, n):
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(0, m+1):
        for j in range(0, n+1):
            if i == 0 or j == 0:
                L[i][j]=0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    i = m
    j = n
    lcs = []
    while(i> 0 and j>0):
        print X[i-1],Y[j-1]
        print i,j
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i = i -1
            j = j -1
        elif L[i-1][j] > L[i][j-1]:
            i = i -1
        else:
            j = j -1

    return L[i][j], lcs[::-1]



def lcs_dynamic(X, Y):
    return lcs_helper_dynamic(X, Y, len(X), len(Y))

print lcs_dynamic("MAN", "CHIMPANZEE")
