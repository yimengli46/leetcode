"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: 
            return 
        
        Q = deque([node])
        mapper = dict()
        while Q:
            nd = Q.popleft()
            
            if nd not in mapper:
                mapper[nd] = Node(nd.val)
                
            for nei in nd.neighbors:
                if nei not in mapper:
                    mapper[nei] = Node(nei.val)
                    Q.append(nei)
                mapper[nd].neighbors.append(mapper[nei])
                
        return mapper[node]