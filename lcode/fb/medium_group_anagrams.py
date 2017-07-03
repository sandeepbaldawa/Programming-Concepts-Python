'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''

Sorting would take O(n * m log m) where n is the number of strings, and m is the length of each string. 
However below takes O(n * m)

'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        mp, res = {}, []
        count = 0
        for str in strs:
            key = 1
            for ch in str:
                key *= primes[ord(ch) - ord('a')]
            if mp.get(key) is None:
                mp[key] = count
                res.append([str])
                count += 1
            else:
                res[mp[key]].append(str)

        return res
            
