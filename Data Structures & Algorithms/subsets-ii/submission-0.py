'''
What exactly happens when we directly apply Subsets I logic here?
    - Try with [1,2,1,2].
        - Subsets I: At each step, we make a decision. Either include the current number, or skip it. Eventually, this explores the power set, as we wanted.
            - Problem with duplicates: One path through the tree is []->[1]->[1,2]->[1,2]->[1,2]. Another path exists lower in the tree that terminates at an identical leaf node. Subsets I would return both, since they're both leaf nodes as defined by the base condition (recursion depth = len(nums)).
            - One possible solution: use position in array to differentiate. Even if leaf nodes are identical, their path through the tree must differ because they started at different points.
    
Potential steps:
    - Sort list. Then, duplicates will be adjacent to each other.
    - Apply skipping logic from Combination Sum II. When we first encounter an element, we recurse and explore all paths beginning from it. Because next elements are identical, we skip them in the loop; i.e, we do not explore paths beginning with them, because all of them have already been explored.
        - Issue: Cannot simply put Subsets logic in the loop. It creates a lot of duplicates. 


'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        n = len(nums)
        def dfs(idx, path):
            if idx >= n:
                res.append(path[:])
                return

            path.append(nums[idx])
            dfs(idx+1, path)
            path.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            dfs(idx+1, path)

        dfs(0, [])
        return res
        