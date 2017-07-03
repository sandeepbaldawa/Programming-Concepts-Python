class Solution(object):
    def __init__(self):
        self.global_res=[]
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    	self.sub_bitarray(nums, 0, [0] * len(nums))
    	return self.global_res
    
    def sub_bitarray(self, word, word_idx, soFar):
      if word_idx == len(soFar):
        res = []
        for i in range(len(soFar)):
          if soFar[i] == 1:
            res.append(word[i])
        self.global_res.append(res)
        return
      soFar[word_idx] = 0
      self.sub_bitarray(word, word_idx+1, soFar)
      soFar[word_idx] = 1
      self.sub_bitarray(word, word_idx+1, soFar)
