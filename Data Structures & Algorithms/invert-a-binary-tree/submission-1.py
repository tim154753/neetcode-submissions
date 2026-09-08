# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Probably some kind of recursion. 
    - Base case: left and right are None. Return parent node.
    - Otherwise:
        - parent.left = Switch(right)
        - parent.right = Switch(left)
        or sum sum like dat
'''


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def switchLR(node):
            if node is None:
                return node
            else:
                temp = node.left
                switchLR(node.right)
                node.left = node.right
                switchLR(temp)
                node.right = temp
        switchLR(root)
        return root