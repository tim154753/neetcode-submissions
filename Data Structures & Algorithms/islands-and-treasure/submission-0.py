'''
Need to reverse mindset of how to find path. Need to find treasure chest and branch out from it.
'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        distances = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))

        def bfs(q):
            visited = set()
            while q:
                r, c = q.popleft()
                cur_dist = grid[r][c]
                for dr, dc in distances:
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and grid[r+dr][c+dc] > 0 and (r+dr, c+dc) not in visited:
                        visited.add((r+dr, c+dc))
                        grid[r+dr][c+dc] = min(grid[r+dr][c+dc], cur_dist + 1)
                        q.append((r+dr, c+dc))
                cur_dist += 1
        bfs(q)

