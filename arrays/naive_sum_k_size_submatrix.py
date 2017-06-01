def sumSubSquares(arr, k):
  ''' Sum of all sub squares of size k
      args: arr
      return : sum

      Clarification
      ==============
      Square matrix i.e. row == col

      Tests
      =====
        Empty
        K > n

      Algo
      ====
      sum = 0
      row 1...n-K+1
        col 1...n-K+1
          sub_row row..row+k
            sub_col col..col+k
              sum+=arr[sub_row][sub_col]
      Time
      =====
      O(N^2*K^2)
     
      Space
      =====
      O(1)
  '''
  if k > len(arr):
    return

  n = len(arr[0])
  res = []
  for row in range(0, n-k+1):
    for col in range(0, n-k+1):
      sum = 0
      for sub_row in range(row, row + k):
         for sub_col in range(col, col + k):
            sum += arr[sub_row][sub_col]
      res.append(sum)

  return res
mat = [[1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5],
      ]   

print sumSubSquares(mat, 3)
