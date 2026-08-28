from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums).values()
        if len(counts) != len(nums):
            return True
        else:
            return False


        