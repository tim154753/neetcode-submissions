'''
Can we make a maxheap with the root always the kth largest rather than largest?
    - I'm imagining something like a linked list of k-1 values attached to a heap.

After hints:
    - instead of a maxheap, use a minheap with k elements. Until we reach k elements, kth largest is just the root of the heap. Afterwards, we can use heap.pushpop(node) to push the new node and pop the smallest node. We do this because after pushing, the smallest node will be the k+1 largest.
    - Should work for stream, but what about initialization with nums? Heapifying it would take O(n) time. Can we do that?
        - Apparently yes. 
        - How do we limit heap to only top k elements, though? 
            - Goofy approach would be to heapify and pop until heap size is k. 
'''
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif (val > self.nums[0]):
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
        