from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # LIFO - Push to tail/add to end
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # Delete head
    def dequeue(self):
        if self.size > 0:
            # Save head node
            head = self.storage.head
            # Delete head
            self.storage.delete(head)
            self.size -= 1
            # Return head value
            return head.value
        else:
            return None

    def len(self):
        return self.size
