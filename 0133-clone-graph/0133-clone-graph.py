
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mapping = {}
        def dfs(node):
            if not node: return
        
            if node in mapping:
                return mapping[node]
            
            
            temp = Node(node.val,[])
            mapping[node] = temp 
                
               
            for i in node.neighbors:  
                temp.neighbors.append(dfs(i))    

            return temp  
        

        return dfs(node)
         