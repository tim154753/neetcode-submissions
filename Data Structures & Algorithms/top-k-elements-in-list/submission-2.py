from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).items()
        rev_counts = {}
        for key, value in counts:
            if rev_counts.get(value) is None:
                rev_counts[value] = [key]
            else:
                rev_counts[value].append(key)

        top = []
        while len(top) != k:
            cur_max = rev_counts.pop(max(rev_counts.keys()))
            top.extend(cur_max)
        return top

            