'''
There will not be extra courses in prerequisites, but there could be less. In any case, we just need to detect cycles in prerequisites.

Step 1:
    - turn prerequisites into an adjacency list
Step 2:
    - run cycle detection algorithm on it. Return False if there is one, otherwise return True
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        def dfs(adj, u, visited, rec):
            if rec[u]:
                return True
            if visited[u]:
                return False
            
            visited[u] = True
            rec[u] = True

            if adj[u]:
                for v in adj[u]:
                    if dfs(adj, v, visited, rec):
                        return True
            rec[u] = False
            return False
        visited, rec = [False]*numCourses, [False]*numCourses
        for v in range(len(adj)):
            if dfs(adj, v, visited, rec):
                return False
        return True

            
        