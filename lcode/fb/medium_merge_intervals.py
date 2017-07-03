'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        res = []
        for idx, pair in enumerate(sorted(intervals, key=lambda x:x.start)):
            if not idx:
                c_s, c_e = pair.start, pair.end
                first = False
            else:    
            	if pair.start <= c_e:
                	c_e = max(c_e, pair.end)
            	else:
                	res.append([c_s, c_e])
                	c_s, c_e = pair.start, pair.end
        
        if not res or res[-1][1] != c_e:
            res.append([c_s, c_e])
            
                
    	return res
