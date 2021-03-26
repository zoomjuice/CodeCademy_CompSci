"""
Nodes Python Setter

We are only allowing the value of the node to be set upon creation. However, we want to allow updating the link of the
 node. For this, we will use a setter to modify the self.link_node attribute.

The method should be called .set_link_node() and should take link_node as an argument. It should then update the
 self.link_node attribute as appropriate.

"""


class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, new_node):
        self.link_node = new_node
