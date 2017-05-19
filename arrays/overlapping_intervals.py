'''
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration
 dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return null.
input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: null # since there is no common slot whose duration is 12
'''
# Below works only because intervals are sorted
def meetingPlanner(slotsA, slotsB, dur):
    iA, iB = 0, 0
    while(iA < len(slotsA) and iB < len(slotsB)):
        start = max(slotsA[iA][0], slotsB[iB][0])
        end = min(slotsA[iA][1], slotsB[iB][1])
        if start + dur <= end:
           return [start, start  + dur]

        if slotsA[iA][0] < slotsB[iB][0]:
           iA+= 1
        else:
           iB+= 1
    return None

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
print meetingPlanner(slotsA, slotsB, 12)
