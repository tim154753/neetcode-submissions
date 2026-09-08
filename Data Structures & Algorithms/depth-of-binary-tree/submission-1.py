# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#prolly just record max recursion depth of DFS or BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def DFS(node):
            depth = 0
            if not node:
                return 0
            else:
                depth = depth + 1 + max(DFS(node.right), DFS(node.left))
            return depth
        return DFS(root)
        
                