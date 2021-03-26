"""
The final use case we mentioned was the ability to remove an arbitrary node with a particular value. This is slightly
 more complex, since a couple of special cases need to be handled.

Consider the following list:

a -> b -> c

If node b is removed from the list, the new list should be:

a -> c

We need to update the link within the a node to match what b was pointing to prior to removing it from the linked list.

Lucky for us, in Python, nodes which are not referenced will be removed for us automatically. If we take care of the
 references, b will be “removed” for us in a process called Garbage Collection.

For the purposes of this lesson, we’ll create a function that removes the first node that contains a particular value.
 However, you could also build this function to remove nodes by index or remove all nodes that contain a given value.
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

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def get_head_node(self):
        return self.head_node

    def stringify_list(self):
        current_node = self.get_head_node()
        list_list = []
        while current_node:
            list_list.append(str(current_node.get_value()))
            current_node = current_node.get_next_node()
        return '\n'.join(list_list)

    def remove_node(self, remove_value):
        current_node = self.head_node
        if current_node.value == remove_value:
            current_node = self.head_node.get_next_node()
            self.head_node = current_node
        while current_node:
            if current_node.get_next_node().get_value() == remove_value:
                current_node.set_next_node(current_node.get_next_node().get_next_node())
                current_node = None
            else:
                current_node = current_node.get_next_node()
