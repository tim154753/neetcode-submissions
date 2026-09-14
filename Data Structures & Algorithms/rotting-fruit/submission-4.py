'''
Basically need 
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        distances = [[1,0], [-1,0], [0,1], [0,-1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))

        def bfs(q):
            visited = set()
            maxtime = 0
            while q:
                r, c = q.popleft()
                visited.add((r,c))
                curr = grid[r][c]
                for dr, dc in distances:
                    nr = r+dr
                    nc = c+dc
                    if nr>=0 and nr<ROWS and nc>=0 and nc<COLS and (nr, nc) not in visited and grid[nr][nc] != 0 and grid[nr][nc] != 2:
                        q.append((nr, nc))
                        visited.add((nr,nc))

                        grid[nr][nc] = 1+curr
                        maxtime = max(maxtime, 1+curr)
            return maxtime
        bfs(q)
        maxtime = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
                maxtime = max(maxtime, grid[row][col])
        return max(maxtime-2, 0)
                
                


        