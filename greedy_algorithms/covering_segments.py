'''
Problem Introduction
You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that
each segment contains at least one marked point.
Problem Description
Task. Given a set of n segments {[a0, b0], [a1, b1], . . . , [an−1, bn−1]} with integer coordinates on a line, find
the minimum number m of points such that each segment contains at least one point. That is, find a
set of integers X of the minimum size such that for any segment [ai
, bi
] there is a point x ∈ X such
that ai ≤ x ≤ bi
.
Input Format. The first line of the input contains the number n of segments. Each of the following n lines
contains two integers ai and bi (separated by a space) defining the coordinates of endpoints of the i-th
segment.
Constraints. 1 ≤ n ≤ 100; 0 ≤ ai ≤ bi ≤ 109
for all 0 ≤ i < n.
Output Format. Output the minimum number m of points on the first line and the integer coordinates of
m points (separated by spaces) on the second line. You can output the points in any order. If there
are many such sets of points, you can output any set. (It is not difficult to see that there always exist
a set of points of the minimum size such that all the coordinates of the points are integers.)
Time Limits. C: 1 sec, C++: 1 sec, Java: 1.5 sec, Python: 5 sec.
Memory Limit. 64Mb.
Sample 1.
Input:
3
1 3
2 5
3 6
Output:
1
3
Explanation:
In this sample, we have three segments: [1, 3], [2, 5], [3, 6] (of length 2, 3, 3 respectively). All of them
contain the point with coordinate 3: 1 ≤ 3 ≤ 3, 2 ≤ 3 ≤ 5, 3 ≤ 3 ≤ 6.
Sample 2.
Input:
4
4 7
1 3
2 5
5 6
Output:
2
3 6
Explanation:
The second and the third segments contain the point with coordinate 3 while the first and the fourth
'''

# Uses python3
# Algorithm
# Sort by end points
# Keep eliminating all segments that are covered by the end point
# Until you have no segments left

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here

    # Sort segments by end point
    segments.sort(key=lambda x: x[1])

    #Keep looping till segments exist
    while(segments):
        # Select first point in the sorted list
        point_selected=segments[0]
        p_end = point_selected.end
        segments.remove(point_selected)
        points.append(point_selected.end)

        remove=[]
        for s in segments:
            #Add to result
            if s.start <= p_end and s.end >= p_end:
                remove.append(s)
        for each in remove:
            segments.remove(each)


    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #segments = [Segment(start=1, end=3), Segment(start=2, end=5), Segment(start=3, end=6)]
    points = optimal_points(segments)
    print(len(points))
    for p in points:
      print(p, end=' ')

