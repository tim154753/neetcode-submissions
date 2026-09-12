'''
Step 1:
    - Identify what decision we make and then backtrack from. 
        - Choose element in list. Add it to potential summation list.
        - Or, don't choose element and skip to next one?
    
Visualization:
    - We start out with empty list. From here, either add first element (right path), or don't (left path). 
    - From right path, again choose whether to add another first element (right path), or don't (left path).
    - From left path, choose whether to add second element (right path), or don't (left path)

nums = [2,5,6,9]
                                                    []
                                            []               [2]
                                        []      [5]     [2]       [2, 5]
                                    []      [6]
'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res, sol = [], []
        def backtrack(i):
            if sum(sol) == target:
                res.append(sol[:])
                return
            elif sum(sol) > target or i == n:
                return
            
            #Decision at each step: either add another nums[i], or add nums[i+1]
            backtrack(i+1) #Go to nums[i+1]

            sol.append(nums[i])
            backtrack(i)
            sol.pop()
        backtrack(0)
        return res


