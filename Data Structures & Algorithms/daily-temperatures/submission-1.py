
'''
Brute force:
    - At each i, iterate through list until we find index with higher temp. 

How can a stack help?
    - Under what conditions do we add an element to the stack?
        - What about if it is greater than the element before it?
'''

from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        warmer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and (temp > temperatures[stack[-1]]):
                idx = stack.pop()
                warmer[idx] = i - idx
            stack.append(i)
        return warmer
            