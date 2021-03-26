"""
Nodes Python Introduction

Now that you have an understanding of what nodes are, let’s see one way they can be implemented using Python.

We will use a basic node that contains data and one link to another node. The node’s data will be specified when
 creating the node and immutable (can’t be updated). The link will be optional at initialization and can be updated.

Remember that at the end of a node path, the link to the next node is null because there are no more nodes left. In
 Python, this means it will be set to None.

"""


class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
