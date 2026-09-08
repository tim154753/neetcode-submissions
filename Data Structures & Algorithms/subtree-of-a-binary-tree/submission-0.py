# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Use same tree logic from last exercise. Since we have O(m*n) time, for each node n we can check in O(m) time if it is the root of a subtree identical to the other tree. Just need to adjust the stopping conditions a bit.

'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node1, node2):
            if not (node1 and node2):
                return node1 == node2
            else:
                return node1.val == node2.val and sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
        def explore(node, subRoot):
            if not node:
                return False
            else:
                return sameTree(node, subRoot) or explore(node.left, subRoot) or explore(node.right, subRoot)
        return explore(root, subRoot)
            