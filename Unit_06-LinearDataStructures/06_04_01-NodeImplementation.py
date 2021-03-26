"""
Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes. So
 before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to
 build our data containers.

Remember that a node contains two elements:

    data
    a link to the next node

Ready? Let’s get started!
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node


my_node = Node(44)
print(my_node.value)
