"""
Stacks Python Size II

It’s time to add a couple helper methods.

Helper methods simplify the code we’ve written by abstracting and labeling chunks of code into a new function. Example:

# Adding "!" without a helper
saying = "I love helper methods"
exclamation = saying + "!"

# Adding "!" with a helper
def add_exclamation_to_string(str):
  return str + "!"

exclamation2 = add_exclamation_to_string("I love helper methods")

This might seem like a silly example, but think about the benefit of the add_exclamation_to_string() helper.

    The name tells us what this function does. Without a helper, we’d need to read the code to understand its meaning.
    The function lets us repeat this behavior. Without a helper, we’d need to keep rewriting the same code!

First, we want to see if our stack has room for more items in .push() to guard against adding them if the stack is full.

Second, it’s helpful to have a method that checks if the stack is empty…
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print('Error: Can\'t push to a full stack.')

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item.get_value()
            self.top_item = self.top_item.get_next_node()  # Garbage collection deletes the old top item once removed
            self.size -= 1
            return item_to_remove
        else:
            print('Error: Nothing in the stack to pop.')

    def peek(self):
        if not self.is_empty():
            return self.top_item.value
        else:
            print('Error: Nothing in the stack to peek at.')

    # Should be inverted to is_full to be more consistent with is_empty()
    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0
