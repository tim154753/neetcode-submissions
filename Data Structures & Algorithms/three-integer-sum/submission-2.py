'''
Recommended: O(N^2). Easy then, I think.
- Step 1: Sort (O(NlogN) time, can be O(1) space)
- Step 2: Iterate through nums. At nums[i], use TwoSum II method from last problem on nums[except i] to determine if there are two other numbers in list that add to -1 * nums[i]. This is O(n) time, O(1) space for each check, with n checks total. 

'''

from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = {}
        for i, num in enumerate(nums):
            target = -1 * num
            front = i+1
            back = len(nums) - 1
            while front < back:
                cur = nums[front] + nums[back]
                if cur > target:
                    back -= 1
                elif cur < target:
                    front += 1
                else:
                    if triplets.get(frozenset(Counter([num, nums[front], nums[back]]))) is not None:
                        next
                    else:
                        triplets[frozenset(Counter([num, nums[front], nums[back]]))] = [num, nums[front], nums[back]]
                    front += 1
        return list(triplets.values())

