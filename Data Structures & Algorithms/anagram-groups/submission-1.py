from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = []
        n = {}
        if len(strs) < 2:
            return [strs]
        for word in strs:
            m.append(frozenset(Counter(word).items()))
        for i, count in enumerate(m):
            if n.get(count) is None:
                n[count] = [strs[i]]
            else:
                n[count].append(strs[i])
        return list(n.values())
            