"""
Stacks Python Size I

With stacks, size matters. If we’re not careful, we can accidentally over-fill them with data. Since we don’t want any
 stack overflow, we need to go back and make a few modifications to our methods that help us track and limit the stack
 size so we can keep our stacks healthy.

What do we do if someone tries to peek() or pop() when our stack is empty?

How do we keep someone from push()ing to a stack that has already reached its limit?

How do we even know how large our stack has gotten?
"""
from node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item

    def pop(self):
        if self.size != 0:
            item_to_remove = self.top_item.get_value()
            self.top_item = self.top_item.get_next_node()  # Garbage collection deletes the old top item once removed
            self.size -= 1
            return item_to_remove
        else:
            print('Error: Nothing in the stack to pop.')

    def peek(self):
        if self.size != 0:
            return self.top_item.value
        else:
            print('Error: Nothing in the stack to peek at.')
