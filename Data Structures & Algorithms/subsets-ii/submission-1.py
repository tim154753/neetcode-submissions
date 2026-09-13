class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []
        n = len(nums)
        def dfs(idx):
            res.append(sol[:])
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                sol.append(nums[i])
                dfs(i+1)
                sol.pop()
        dfs(0)
        return res