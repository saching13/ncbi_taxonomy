# Lowest common ancestor for taxonomy dataset

The algorithm can be repurposed for any other datasets that fits tree data structure but you need to pass the edges, nodes and weights as follows.

## Edges
    Create directed edges from child node to parent node with weights if necessary. 
    For Ex: 
    {
        child_node1:(parent_node1, weight1, weight2,...)
        child_node2:(parent_node1, weight1, weight2,...)
        .
        .
        .
    }
    if you don't have any weights add None to that Ex: {child_node1:(parent_node1, None)..}

## Nodes
    Here we need to get the list of unique nodes, however that is being handled. To get nodes
    along with nodes information you need to pass the dataframe with node id / node name which 
    should be same as node id / node names used in creating edges. Along with this dataframe you need 
    to pass the name of the column which containes the node id / node names in the given data frame.


#### [FinalAncestorReport.ipynb](./FinalAncestorReport.ipynb) 
Check the above file to see how taxonomy dataset from ncbi taxanomy is exploted to create edges and pass it to tree class and get the lowest common ancestor and other information


#### [graph.py](./graph.py) 
This file contains the `Tree` class which takes nodes, edges with or without weights and comes with functions to get lowest common ancestor of given nodes, edge info. and node info. Feel free to take a look over the implementation.


### Dataset
Download the dataset [here](https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz) <br /> 
**names.dmp** and **nodes.dmp** files are used in this project <br /> 
For more information check [here](https://www.ncbi.nlm.nih.gov/taxonomy) <br /> 
