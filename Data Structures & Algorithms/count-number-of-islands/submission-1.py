'''
Step 1 is probably to turn grid into a graph. 
        - Nodes are coordinates in grid. Edge exists between nodes if they are land and neighbor each other. Land coords are also connected to themselves.
'''
from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = defaultdict(list)
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    adj[(row, col)].append((row,col))
                    if row > 0 and grid[row-1][col] == '1':
                        adj[(row, col)].append((row-1, col))
                    if row < len(grid) - 1 and grid[row+1][col] == '1':
                        adj[(row, col)].append((row+1, col))
                    if col > 0 and grid[row][col-1] == '1':
                        adj[(row, col)].append((row, col-1))
                    if col < len(grid[0]) - 1 and grid[row][col+1] == '1':
                        adj[(row, col)].append((row, col+1))

        def dfs(coord):
            if coord in visited or grid[coord[0]][coord[1]] == '0':
                return
            visited.add(coord)
            for neighbor in adj[coord]:
                dfs(neighbor)


        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs((row,col))
                    islands += 1
        return islands

                
                