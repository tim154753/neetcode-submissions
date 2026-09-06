'''
Just find the pivot element. The minimum should be right after it.
    - Easy to do in O(n). Just find max. Min is after it.
    - O(log(n)) solution requires us to utilize the partially sorted quality of the array. 
        - Split it in half. Three cases:
            - We split between the rotated halves, in which case left side[-1] is greater than right[0]. Then the minimum is just right[0].
            - We split inside a sorted section, meaning left[-1] < right[0]. Then, we can find which half to split again by checking left[-1] vs right [-1]. 
                - If right[-1] < left[-1], split list again on the right (midpoint between mid and end of list)
                - Otherwise, split on left.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r+l)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return nums[l]