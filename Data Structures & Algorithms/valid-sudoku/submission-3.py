from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            counts = Counter(row)
            counts.pop('.', None)
            if any(freq > 1 for freq in counts.values()):
                return False
        for i in range(len(board)):
            col = [row[i] for row in board]
            counts = Counter(col)
            counts.pop('.', None)
            if any(freq > 1 for freq in counts.values()):
                return False
        for i in range(3):
            for j in range(3):
                square = board[3*i:3*(i+1)]
                square = [row[3*j:3*(j+1)] for row in square]
                counts = Counter(num for sublist in square for num in sublist)
                counts.pop('.', None)
                if any(freq > 1 for freq in counts.values()):
                    return False
        return True