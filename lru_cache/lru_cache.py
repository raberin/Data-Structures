from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.cache = {}
        self.dll = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # If there's no value return None
        if key not in self.cache:
            return None
        else:
            # Move the node that we're retrieving to tail
            value = self.cache[key].value[1]
            self.dll.move_to_end(self.cache[key])
            return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # If size == limit remove from head and decrement
        if self.size == self.limit and key not in self.cache:
            head = self.dll.head
            to_be_deleted_key = head.value[0]
            # Delete Head from DLL
            self.dll.delete(head)
            # Delete Key:value pair from cache
            del self.cache[to_be_deleted_key]
            # decrement
            self.size -= 1
        # if key already exists in cache, overwrite the value and move to tail
        if key in self.cache:
            # Overwrite the value of that node
            self.cache[key].value = (key, value)
            # Move node to tail
            self.dll.move_to_end(self.cache[key])
        else:
            # Set a key in cache, set value to be added to tail in DLL
            # Create a tuple for value so it stores key AND value
            my_node_value = (key, value)
            self.dll.add_to_tail(my_node_value)
            self.cache[key] = self.dll.tail
            self.size += 1
