'''
Easiest method:
    - Find pivot using method from last problem. (O(log(n)))
    - Find which half the target would be in by comparing target to min of right half = element after pivot (O(1))
    - Binary search on this half (O(log(n)))

Must be a way to do everything in one loop though, right?
    - Instead of directly looking for pivot, we use the invariant that for any mid, one half of mid is sorted, other half contains pivot.
    - Can determine if sorted half contains target in O(1) time.
    - If it does, then set l and r accordingly and binary search.
    - Otherwise, discard that half. 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]: #then l:mid is the sorted half
                if target < nums[mid] and target >= nums[l]: #target is in this half
                    r = mid-1
                else:
                    l = mid+1
            else: #then mid:r is the sorted half
                if target <= nums[r] and target > nums[mid]: #target is in this half
                    l = mid + 1
                else:
                    r = mid-1
        return -1

