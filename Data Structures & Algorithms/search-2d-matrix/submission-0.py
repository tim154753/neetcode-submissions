class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        n = len(matrix[0])
        def coordTranslate(n,idx):
            row = idx//n
            col = idx%n
            return row, col


        while l <= r:
            mid_row, mid_col = coordTranslate(n, (l+r)//2)
            if target == matrix[mid_row][mid_col]:
                return True
            elif target < matrix[mid_row][mid_col]:
                r = (l+r)//2 - 1
            elif target > matrix[mid_row][mid_col]:
                l = (l+r)//2 + 1
        return False
            
