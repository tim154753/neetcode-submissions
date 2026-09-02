'''
Note: list is sorted!
- Binary search is O(log(n)), so a naive solution would be to iterate through nums and use binary search to see if target-num is in list. This would be O(nlogn).

- Optimizations:
    - After each num, if target-num is not in list, ignore it for next checks.
        - Still doesn't get us down to O(n), but maybe on the right track?
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        while front != back:
            cur = numbers[front] + numbers[back]
            if cur == target:
                return [front+1, back+1]
            elif cur < target:
                front += 1
            elif cur > target:
                back -= 1
