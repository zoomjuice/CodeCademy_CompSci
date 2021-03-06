"""
Stacks Python Introduction

You have an understanding of how stacks work in theory, so now let’s see how they can be useful out in the wild!

Remember that there are three main methods that we want our stacks to have:

    Push - adds data to the “top” of the stack
    Pop - provides and removes data from the “top” of the stack
    Peek - provides data from the “top” of the stack without removing it

We also need to consider the stack’s size and tweak our methods a bit so that our stack does not “overflow”.

Let’s get started building out our Stack class.
"""


class Stack:
    def __init__(self):
        self.top_item = None

    def peek(self):
        return self.top_item.value
