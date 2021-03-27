"""
Stacks Python Push and Pop

The stack’s push() and pop() methods are our tools to add and remove items from it. pop() additionally returns the
 value of the item it is removing. Keep in mind that we can only make modifications to the top of the stack.
"""
from node import Node


class Stack:
    def __init__(self):
        self.top_item = None

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item

    def pop(self):
        item_to_remove = self.top_item.get_value()
        self.top_item = self.top_item.get_next_node()  # Garbage collection will delete the old top item once removed
        return item_to_remove

    def peek(self):
        return self.top_item.value
