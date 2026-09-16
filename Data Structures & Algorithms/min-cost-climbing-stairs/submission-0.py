class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        memo = {}
        cost.append(0)
        memo[0] = cost[0]
        memo[1] = cost[1]
        def f(x):
            if x in memo:
                return memo[x]
            memo[x] = cost[x]+ min(f(x-2), f(x-1))
            return memo[x]
        return(f(len(cost)-1))