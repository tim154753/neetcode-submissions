'''
    - Definitely need recursion, but not sure how
        - Base case is probably when there's no elements left to append to a subset.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            if i == n: #base case. At this point, we're at a leaf node of the tree we're generating
                res.append(sol[:]) # append a copy of sol, not reference to it
                return
            
            #Path 1: skip current num
            backtrack(i+1)

            #Path 2: include current num
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res