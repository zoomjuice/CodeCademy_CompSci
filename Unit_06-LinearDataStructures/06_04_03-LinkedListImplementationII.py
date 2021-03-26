"""
So far we can:

    create a new LinkedList using .__init__()
    get the head node of the list using .get_head_node()

Next up, we’ll define methods for our LinkedList class that allow us to:

    insert a new head node
    return all the nodes in the list as a string so we can print them out in the terminal!
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


# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
# print(ll.head_node.value)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
