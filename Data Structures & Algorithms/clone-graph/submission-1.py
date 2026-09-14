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
        q = deque()
        
        q.append(node)

        while q:
            for i in range(len(q)):

                cur_node = q.popleft()
                
                if cur_node not in dct:
                    new_node = Node(cur_node.val)
                    dct[cur_node] = new_node
                else:
                    new_node = dct[cur_node]
                

                for n in cur_node.neighbors:
                    new_nei = Node(n.val)
                    if n not in dct:
                        new_node.neighbors.append(new_nei)
                        dct[n] = new_nei
                        q.append(n)
                    else:
                        new_node.neighbors.append(dct[n])
                    


                    
                
        
        return dct[node]




        