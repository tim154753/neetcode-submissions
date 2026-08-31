'''
How to do this without division?

Can easily do it in O(N^2) time. Example:
- [1,2,3,4]
    - Prods[0] = 2*3*4 = 24
    - Prods[1] = 1*3*4 = 12
    - Prods[2] = 1*2*4 = 8
    - Prods[3] = 1*2*3 = 6
- Room for optimization: tons of repeated operations. 
 - What if we store the prefix and suffix product and use them?
    - PreProds = [1, 2, 6, 24]
    - SuffProds = [4, 12, 24, 24]
    - Then, if we want to compute Prods[0], it's just SuffProds[-2] * 1
    - Prods[1] = SuffProds[-3] * PreProds[1]
    - 

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProds = [1]
        suffProds = [1]
        for i in range(len(nums)):
            preProds.append(preProds[i]*nums[i])
            suffProds.append(suffProds[i]*nums[-1-1*i])
        suffProds.reverse()
        prods = [0]*len(nums)
        for i in range(len(nums)):
            prods[i] = preProds[i]*suffProds[i+1] 
        return prods