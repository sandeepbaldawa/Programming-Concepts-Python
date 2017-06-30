'''
A machine accepts jobs at different start and end time.
Write a scheduler which can scheduler these jobs such that
the scheduler is optimally used i.e. the idle times of the
scheduler are minimized
'''



"""
Unweighted Interval scheduling algorithm.
Runtime complexity: O(n log n)
"""

class Interval(object):
    '''Date interval'''

    def __init__(self, start, end):
        self.start = start
        self.finish = end

    def __repr__(self):
        return str(self.start + self.finish)



def schedule_unweighted_intervals(I):
    '''sorting is O(n log n), selecting is O(n)'''

    I = sorted(I, key=lambda x:x.start)
    
    O = []
    finish = 0
    for i in I:
        if finish <= i.start:
            finish = i.finish
            O.append((i.start, i.finish))

    return O

if __name__ == '__main__':
    I = []
    I.append(Interval(9, 10))
    I.append(Interval(9.5, 11))
    I.append(Interval(10.5, 12))
    I.append(Interval(11.5, 13))
    I.append(Interval(14, 15))
    I.append(Interval(7, 8))
    O = schedule_unweighted_intervals(I)
    print O
