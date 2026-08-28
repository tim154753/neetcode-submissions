from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = defaultdict(int)
        if len(s) != len(t):
            return False
        for char in s:
            hash[char] += 1
        nums = list(hash.values())
        for char in t:
            hash[char] += 1
        nums_final = list(hash.values())
        if(len(nums) != len(nums_final)):
            return False
        for k in range(0,len(nums)-1):
            if(2*nums[k] != nums_final[k]):
                return False
        return True
        
        
