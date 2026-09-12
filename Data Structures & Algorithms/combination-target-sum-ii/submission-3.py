class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def dfs(idx, path, cur):
            if cur == target:
                res.append(path[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                elif cur > target:
                    break
                
                path.append(candidates[i])
                dfs(i+1, path, cur+candidates[i])
                path.pop()
        dfs(0, [], 0)
        return res