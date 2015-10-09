def spiral(A, m, n):
    T = 0
    B = m-1
    L = 0
    R = n-1
    dir = 0
    while(T <=B and L<=R):
        if dir == 0:
            for i in range(L,R+1):
                #print T,i
                print A[T][i]
            T+=1
        elif dir == 1:
            for i in range(T,B+1):
                #print i,R
                print A[i][R]
            R-=1
        elif dir == 2:
            for i in range(R,L-1,-1):
                #print B,i
                print A[B][i]
            B-=1
        elif dir == 3:
            for i in range(B,T-1,-1):
                #print i,L
                print A[i][L]
            L+=1
        dir = (dir + 1) % 4




arr = [[1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]]
print arr
spiral(arr, 4, 4)
