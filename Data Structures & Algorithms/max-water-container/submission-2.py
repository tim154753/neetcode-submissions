'''
Obvious O(N^2) solution:
    - initialize best as 0
    - at each height[i], compute area with each height starting with i+1. Note: area = min(i,j) * (j-i).
    - if area > best, update best as area. 

Potential optimizations: 
    - if height[i+1] <= height[i], we can completely skip it.
        - does this make it O(n)?
            - No. Worst case: list is in ascending order, so each element takes n-i checks.
    - if height[i+1] <= height[j], where height[j] is the height of the other bar used in the current max, we only need to check the area formed by height[i+1] and height[j].
        - why? Actually, NOT TRUE I THINK
        - Does this make it O(n)? Probably not, because we still have two for loops. Probably some edge case that can make it O(N^2).
    - find argmax(heights). The rightmost bar in the optimal solution is either here or after it.
        - if tallest bar is already at the end, this optimization doesn't do anything, so it also doesn't make it O(n).
    - 
    - Two pointers?
        - l = 0, r = len(heights) - 1. Calculate area: min(height[l], height[r])*r-l. 
        - With what conditions do we move the pointers? Not obvious.

'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers attempt:
        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            area = min([heights[l], heights[r]])*(r-l)
            if area > best:
                best = area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return best
            