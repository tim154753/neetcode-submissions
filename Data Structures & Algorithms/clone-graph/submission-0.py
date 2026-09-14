"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Recursion probably works best here. We probably need to recurse until we reach a "leaf" node, as in, it either has no neighbors or its neighbors have all already been visited. In that case, we append either nothing or the new nodes that we saw earlier in recursion as its neighbors, and return.
    - Issue: how can a node seen at a deeper level of recursion append a value from a higher level? 
        - Maybe initialize a global list of visited nodes so a node can grab them as needed and append to its neighbor list.
'''

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        stack = deque()
        stack.append(node)
        visited.add(node)
        head = node

        clone = {}

        def dfs(node):
            if not node:
                return
            nodeClone = Node(node.val)
            clone[node] = nodeClone
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
                nodeClone.neighbors.append(clone[neighbor])
            return
        dfs(head)
        return clone.get(head, None)

