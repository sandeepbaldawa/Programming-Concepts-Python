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
class Interval():
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{0}, {1}]".format(self.start, self.end)

class Solution:
    def merge_intervals(self, input):
        if not input:
            return input
        input = sorted(input, key=lambda x:x.start)
        result=[input[0]]
        for i in range(len(input)):
            current = input[i]
            if current.start <= result[-1].end:
                result[-1].end = max(result[-1].end, current.end)
            else:
                result.append(current)
        return result


        return res

def print_input(res1):
    for each in res1:
        print each.start, each.end

print Solution().merge_intervals([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(9, 12), Interval(15,18)])
