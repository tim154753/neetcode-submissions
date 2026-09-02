class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        best = 0
        for num in setNums:
            if num-1 not in setNums:
                streak = 1
                while (num+streak) in setNums:
                    streak += 1
                if streak > best:
                    best = streak
        return best
        