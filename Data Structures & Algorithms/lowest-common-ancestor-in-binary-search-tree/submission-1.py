# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Rough idea:
    - Find p and q each in logn time. Record paths, trace back until we find a match.
        - 2*logn = h to find, h to trace back
    - Or, could we look for both at once and just return the first node at which they diverge?
        - O(h) time but O(1) space I think?
            - maybe iteratively, recursively would be O(h)
'''

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findLCA(node, p, q):
            if p.val == node.val or q.val == node.val:
                return node
            if (p.val<node.val) ^ (q.val<node.val):
                return node
            else:
                if p.val < node.val:
                    return findLCA(node.left, p, q)
                else:
                    return findLCA(node.right, p, q)
        return findLCA(root, p, q)

