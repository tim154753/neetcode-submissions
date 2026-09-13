'''
Ideas:
    - How does backtracking help?
        - Rough sketch: at each step, we make a choice of which element to include in array. For example. []->1,2,3?->[1]->2,3?->[1,2]->3?->[1,2,3]. Backtracking, we go back up to [1] to make a different choice [1]->2,3?->[1,3]->2?->[1,3,2]. Now, there's no choices left to make for 1, so we backtrack up to [] and make a different choice []->1,2,3?->[2], and so on.
        -Then, at each level i of the tree, there are len(nums) - i choices to make for each node. Then there are n! possible nodes. 
        - Are we automatically preventing duplicates? Probably
        - Within each call to function, we should pass the list of valid choices
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        choices = nums[:]
        def backtrack(choices):
            if not choices:
                res.append(sol[:])
                return
            
            for i in range(len(choices)):
                a = choices.pop(i)
                sol.append(a)
                backtrack(choices)
                sol.pop()
                choices.insert(i, a)
        backtrack(choices)
        return res
