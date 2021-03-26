"""
Linked List Review

Congratulations, you have implemented a linked list in Python!

We did this by:

    Defining a Node class to hold the values and links between nodes
    Implementing a LinkedList class to handle external operations on the list like adding and removing nodes

Feel free to play around a bit with your code. Here are some ideas:

    Create a few nodes and adding them to a new linked list
    Print your linked list out by using your stringify_list() method
    Remove your linked list’s head node
    Print your list again — was your original head node removed?
    So far you’ve built a method to remove the first occurrence of a given value. How do you think you would remove all
     nodes that have a specific value? Try building a method to do that!
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
