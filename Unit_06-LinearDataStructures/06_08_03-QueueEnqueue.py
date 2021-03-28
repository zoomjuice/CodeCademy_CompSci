"""
Queues Python Enqueue

“Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the enqueue() method.

There are three scenarios that we are concerned with when adding a node to the queue:

    The queue is empty, so the node we’re adding is both the head and tail of the queue
    The queue has at least one other node, so the added node becomes the new tail
    The queue is full, so the node will not get added because we don’t want queue “overflow”

Let’s put this into action by building out an enqueue() method for Queue.
"""
from node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print('Adding ' + str(item_to_add.get_value()) + ' to the queue!')
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print('error: tried to enqueue to full queue')

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        print('error: tried to peek at empty queue')

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.size < self.max_size

    def is_empty(self):
        return self.size == 0


q = Queue()
q.enqueue('foo')
