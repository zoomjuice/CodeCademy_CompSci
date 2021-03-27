"""
Stacks Python Review

Nice work — you’ve built out a Stack class that can:

    add a new item to the top via a push() method
    remove an item from the top and returns its value with a pop() method
    return the value of the top item using a peek() method
    allows a stack instance to maintain an awareness of its size to prevent stack “overflow”

So how does your code stack up against pizza delivery?
"""
from node import Node


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
            print("Adding {} to the pizza stack!".format(value))
        else:
            print('Error: Can\'t push to a full stack.')

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item.get_value()
            self.top_item = self.top_item.get_next_node()  # Garbage collection deletes the old top item once removed
            self.size -= 1
            print("Delivering " + item_to_remove)
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


# Defining an empty pizza stack with limit of 6
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have a full stack
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()
