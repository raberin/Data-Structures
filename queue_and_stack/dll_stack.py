from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    # Push to end of DLL
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # Remove the tail
    def pop(self):
        # Check if there are nodes
        if self.size > 0:
            value = self.storage.remove_from_tail()
            self.size -= 1
            return value
        else:
            return None

    def len(self):
        return self.size
