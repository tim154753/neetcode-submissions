# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Just return furthest right node from level-wise traversal
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = deque()
        nodes.append(root)
        visited = []
        while nodes:
            visited.append(0)
            curr = len(nodes)
            for i in range(curr):
                node = nodes.popleft()
                if node:
                    visited[-1]=(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
        return visited[:-1]