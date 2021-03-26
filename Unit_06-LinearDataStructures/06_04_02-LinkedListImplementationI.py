"""
With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a
 variety of methods can be defined.

For our use, we want to be able to:

    get the head node of the list (it’s like peeking at the first item in line)
    add a new node to the beginning of the list
    print out the list values in order
    remove a node that has a particular value
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


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node


my_linkedlist = LinkedList(44)
print(my_linkedlist.get_head_node().value)
