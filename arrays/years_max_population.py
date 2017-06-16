'''
Given input set of years, return the range of
years where the population was the max

eg:- 2000, 2010
     1975, 2005
     1975 2003
     1803 1809
     1750 1869
     1803 1921
     1894 1921

Between 1750 to 1921 => 4 people were born
Between 1975 to 2010 => 3 people were born

'''

class Interval():
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{0}, {1}]".format(self.start, self.end)

def max_population_years(input):
    '''Return years which have the maximum population'''
    if input <= 1:
        return input

    input = sorted(input, key=lambda x: x.start)
    res = [input[0]]
    count_array, count = [], 1

    for i in range(1, len(input)):
        if input[i].start <= res[-1].end:
            res[-1].end = max(input[i].end, res[-1].end)
            count += 1
        else:
            count_array.append(count)
            count = 1
            res.append(input[i])
    count_array.append(count)
    print count_array, res
    return res[count_array.index(max(count_array))].start, res[count_array.index(max(count_array))].end


print max_population_years([Interval(2000, 2010), Interval(1975, 2005), Interval(1975, 2003), Interval(1803, 1809), Interval(1750,1869), Interval(1803,1921),Interval(1894,1921)])
print max_population_years([Interval(2000, 2010), Interval(2010, 2015), Interval(2015, 2020)])
