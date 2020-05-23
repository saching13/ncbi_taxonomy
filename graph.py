import numpy as np
import pandas as pd



class Tree:
    """An N-dimentional tree built using dataframe and edges / adjacent list as dictionary which
    consists of functions to return the root node, find the nearest common ancestor of two nodes,
    edge weights or information and node information.
    
    Parameters:
    --------------
    edges = edges consists of all the edges of the graph with directed connection from a specific node to it's parent 
            along with weight represented in the form of dict data structure. 
            Here weight is considered mostly as information from the edge.
            Ex: one edge is in edges => {child_node: (parent node,weight1, weight2,...), ...}
    names_df = names data frame is the dataframe which contains list of nodes in a
                column and rest of the column represents information about the node
    indexName = index name provides the column name of the names_df which is the node name
    """
    
    def __init__(self, edges, names_df, indexName):
        self.edges = edges
        self.nodes = list(names_df[indexName].unique())
        self.nodeInfo = names_df.groupby([indexName])
        self.root = self._rootNode()
        
    def _rootNode(self):
        for node in self.nodes:
            if not self.edges.get(node):
                return node

    def depthFinder(self,curr_node, top_node):
        """ given two nodes provides the depth between the two nodes if a directed path exists between them"""
        depth = 0
        inputNode = curr_node
        while curr_node != top_node:
            curr_node = self.edges.get(curr_node)[0] # Retriving only the parent node from (parent_node,weight1, weight2,...)
            assert(curr_node),f"Path between {inputNode} and {top_node} doesn't exist"
            depth += 1
        return depth

    def backTrackTree(self, distantNode, closestNode, diff):
        """ Helper function to find the ancestor"""
        while diff > 0:
            # Retriving only the parent node from (parent_node,weight1, weight2,...)
            distantNode = self.edges.get(distantNode)[0] 
            diff -= 1
        while distantNode != closestNode:
            distantNode = self.edges.get(distantNode)[0]
            closestNode = self.edges.get(closestNode)[0]
        return distantNode
            
    def findLowestAncestor(self, firstNode, secondNode):
        topAncestor = self.root
        depthFirst = self.depthFinder(firstNode, self.root)
        depthSecond = self.depthFinder(secondNode, self.root)
        diff = depthFirst - depthSecond
        if diff > 0:
            lowestAncestor = self.backTrackTree(firstNode, secondNode, diff)
        else:
            lowestAncestor = self.backTrackTree(secondNode, firstNode, -diff)
        return lowestAncestor

    def getNodeInfo(self,node):
        return self.nodeInfo.get_group(node)

    def edge_info(self, child):
        info = self.edges.get(child)
        assert(info),f"No parent found for child :{child}"
        return info