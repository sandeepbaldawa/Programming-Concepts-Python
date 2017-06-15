'''
Merge overlapping interval

  a------b
c-----d


a---b                     a---------b
  c-----d                   c-----d   
   
   
  c---d
a-----b


c---d                     c---------d
  a-----b                   a-----b
   

a-----b
c-----d

We can reduce some use cases if we sort the start Times
Input => [1,3],[2,6],[8,10],[6,12],[15,18]
Ans => [1,6][8,10][15,18]


'''


def merge_intervals(input):
  res = []
  input = sorted(input, key=lambda x:x[0])
  print input

  prev_start, prev_end = input[0][0], input[0][1]
  res.append([prev_start],[prev_end])
  start = prev_start
  end = prev_end
  for idx in range(1, len(input)):
    curr_start, curr_end = input[idx][0], input[idx][1]
    prev_start, prev_end = res[-1][0], res[-1][1]
   
    if curr_start <= prev_end:
      end = max(prev_end, curr_end)
    else:
      res.append(res[-1][1])
  
  return res
   


res = [1,3],[2,6],[8,10],[6,12],[15,18]
print merge_intervals(res)

