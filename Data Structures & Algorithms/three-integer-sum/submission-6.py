'''
Recommended: O(N^2). Easy then, I think.
- Step 1: Sort (O(NlogN) time, can be O(1) space)
- Step 2: Iterate through nums. At nums[i], use TwoSum II method from last problem on nums[except i] to determine if there are two other numbers in list that add to -1 * nums[i]. This is O(n) time, O(1) space for each check, with n checks total. 

'''

from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = [[None, None, None]]
        last_num = None
        for i, num in enumerate(nums):
            if num == last_num:
                continue
            target = -1 * num
            front = i+1
            back = len(nums) - 1
            while front < back:
                while front < back:
                    cur = nums[front] + nums[back]
                    if cur > target or back == i:
                        back -= 1
                    elif cur < target or front == i:
                        front += 1
                    else:
                        triplet = [num, nums[front], nums[back]]
                        if triplet != triplets[-1]:
                            triplets.append(triplet)
                        front += 1
            last_num = num
        return triplets[1:]

