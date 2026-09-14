class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        distances = [[1,0], [-1,0], [0,1], [0,-1]]

        q = deque()
        fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        maxtime = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in distances:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            maxtime += 1
        
        return maxtime if fresh == 0 else -1
                    