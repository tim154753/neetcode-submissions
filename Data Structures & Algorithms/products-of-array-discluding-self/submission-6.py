        #easy solution: compute prod of all nums, divide nums[i].
'''
Problem: sps only element i is 0. Then prod will be 0, and prods[i] will be 0/0 which is both wrong and throws an error. prods[i] should be nonzero. 

Solution idea: be less mathematical. The issue is that multiplying by 0 removes information, and dividing by 0 attempts to extract information that does not exist. 
- Try to solve each problem:
    - Multiplication by 0: prod is a tuple. One element is the simple result of multiplying all numbers together, even if 0s are present. Other element is the product of all numbers except 0s. Then, if 1 0 is present, we use this product. If more than 1 0 is present, prods should be all 0 anyway. This is a janky solution, but should solve mult and division by 0.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod = prod*num
        prods = [0]*len(nums)
        if zero_count > 1:
            return prods
        for i, num in enumerate(nums):
            if num == 0:
                prods[i] = prod
            else:
                prods[i] = prod//num*(zero_count<1)
        return prods