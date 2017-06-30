# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        queue, dict = [node], {}
        dict[node] = UndirectedGraphNode(node.label)
        
        while(queue):
            curr_node = queue.pop()
            for neighbour in curr_node.neighbors:
                if neighbour in dict:
                    dict[curr_node].neighbors.append(dict[neighbour])
                else:
                    new_node = UndirectedGraphNode(neighbour.label)
                    dict[neighbour] = new_node
                    dict[curr_node].neighbors.append(new_node)
                    queue.append(neighbour)
                    
        return dict[node]            
