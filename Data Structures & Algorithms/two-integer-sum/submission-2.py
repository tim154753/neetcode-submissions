class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            m[num] = [i, target - num]
        for i, num in enumerate(nums):
            v = m.get(target-num)
            if v is not None and v[0] > i:
                return [i, v[0]]


        