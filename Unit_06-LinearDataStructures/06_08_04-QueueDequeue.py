"""
Queues Python Dequeue

We can add items to the tail of our queue, but we remove them from the head using a method known as dequeue(), which is
 another way to say “remove from a queue”. Like enqueue(), we care about the size of the queue — but in the other
  direction, so that we prevent queue “underflow”. After all, you don’t want to remove something that isn’t there!

As with peek(), our dequeue() method should return the value of the head. Unlike, peek(), dequeue() will also remove
 the current head and replace it with the following node.

For dequeue, there are three scenarios that we will take into account:

    The queue is empty, so we cannot remove or return any nodes lest we run into queue “underflow”
    The queue has one node, so when we remove it, the queue will be empty and we need to reset the head and tail to None
    The queue has more than one node, and we just remove the head node and reset the head to the following node
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

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print('error: tried to dequeue from an empty queue')

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
