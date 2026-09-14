"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        dct = {}
        dct[node] = Node(node.val)
        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in dct:
                    dct[n] = Node(n.val)
                    q.append(n)

                dct[cur].neighbors.append(dct[n])

        return dct[node]

        