from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_nums = defaultdict(list)
        for i in nums:
            dup_nums[i].append(i)
            if len(dup_nums[i]) > 1:
                return True
        return False
