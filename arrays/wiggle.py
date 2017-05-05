'''
The wiggle problem, given an array of integers arrange them   such that alternate elements are large and small.(2,5,3,6,...) 
'''

def wiggleSort(nums):
    flag = True
    for i in range(len(nums)-1):
        if (flag and nums[i] > nums[i+1]) or \
           (not flag and nums[i] < nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 1
        flag = not flag
nums = [1,2,8,9,3,5]
print nums
wiggleSort(nums)
print nums
