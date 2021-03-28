"""
Queues Python Size

Bounded queues require limits on the number of nodes that can be contained, while other queues don’t. To account for
 this, we will need to make some modifications to our Queue class so we can keep track of and limit size where needed.

We’ll be adding two new properties to help us out here:

    A size property to keep track of the queue’s current size
    A max_size property that bounded queues can utilize to limit the total node count

In addition, we will add three new methods:

    get_size() will return the value of the size property
    has_space() will return True if the queue has space for another node
    is_empty() will return true if the size is 0
"""


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        print('Error: queue empty')

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.size < self.max_size

    def is_empty(self):
        return self.size == 0
