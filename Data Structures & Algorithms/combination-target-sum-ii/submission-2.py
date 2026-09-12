class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = Counter(candidates)
        n = len(candidates)
        candidates = list(set(candidates))
        res, sol = [], []

        def backtrack(i, cur, counts):
            if cur > target or (i == len(candidates)) or counts[candidates[i]] < 0:
                return

            elif cur == target:
                res.append(sol[:])
                return
            
            backtrack(i+1, cur, counts)

            sol.append(candidates[i])
            counts[candidates[i]] -= 1
            backtrack(i, cur+candidates[i], counts)
            sol.pop()
            counts[candidates[i]] += 1
        backtrack(0,0, counts)
        return res
