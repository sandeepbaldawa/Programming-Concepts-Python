class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m-1, n-1
        while (idx1 >= 0 and idx2 >= 0):
            if nums1[idx1] > nums2[idx2]:
                nums1[idx1 + idx2 + 1] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx1 + idx2 + 1] = nums2[idx2]
                idx2 -= 1
        while(idx2 >= 0):
            nums1[idx1] = nums2[idx2]
            idx2 -= 1
                
           
