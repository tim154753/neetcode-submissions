import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            curr = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if curr != second:
                heapq.heappush(stones, curr-second)
        if not stones:
            return 0
        else:
            return -stones[0]