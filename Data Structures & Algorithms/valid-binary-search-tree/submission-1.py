# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Idea:
    - Recursively check if subtree is a BST by keeping track of most restrictive node in the tree.
        - So, starting from root, check if left subtree is a BST, then left.left, etc and also make sure each node is less than or greater than root of subtree.

Another idea:
    - Inorder traversal of BST (left node right) should produce a sorted list if BST is correct. Just do this traversal and check if the list is sorted, both O(n) time.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(node, res):
            if not node:
                return
            else:
                DFS(node.left, res)
                res.append(node.val)
                DFS(node.right, res)
            return res
        res = []
        DFS(root, res)
        l = 0
        r = 1
        while r < len(res):
            if res[l] >= res[r]:
                return False
            l += 1
            r += 1
        return True

