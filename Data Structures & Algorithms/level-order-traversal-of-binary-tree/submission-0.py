# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Is this not just BFS with a modification to make sure different levels are separated by brackets?
    - bracket separation is the hard part. BFS doesn't have a clear way to do it because there is no "depth", really. We just go left to right. Need to combine level-order scanning of BFS with depth-tracking of DFS.
    - DFS can go pre, in, or post order (root left right, left root right, left right root), none of which are actually level order. pre order is the closest.


BFS:
    - use a queue.
    - while queue not empty
    - add node to queue, then its left and right children.
    - pop node and append to visited list.

    Solution:
        - Use BFS, but keep track of levels by iterating over queue (?)
        - At root, add up to current size to new sublist. So just root. Then add left and right children.
        - Now, iterate up to current size, add to new sublist. Then, add left and right children
'''



from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        nodes.append(root)
        visited = []
        while nodes:
            visited.append([])
            curr = len(nodes)
            for i in range(curr):
                node = nodes.popleft()
                if node:
                    visited[-1].append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
        return visited[:-1]

            