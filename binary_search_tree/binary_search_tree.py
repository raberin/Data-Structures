# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Check if the value is duplicate, return False
        if self.value == value:
            return False
        # If value to be inserted, is less than node.value
        elif value < self.value:
            # If there is a left child, recursively call insert
            # Otherwise insert to the left of current node
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
                return True
        else:
            # If there is a right child, recursively call insert
            # Otherwise insert to the right of current node
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return True

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base Case Return True when value == target
        if self.value == target:
            return True
        else:
            # Recursive Cases
            # If target is greater and there is a right node recurse right
            # Otherwise, return false
            if target > self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
            # If target is less than and there is a left node recurse left
            # Otherwise, return false
            else:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # While there are right child nodes, move right
        while self.right:
            self = self.right
        # Return value
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # Run func in current node
        cb(self.value)
        # If left child present, recursively run func to left nodes
        if self.left:
            self.left.for_each(cb)
        # If right child present, recursively run func to right nodes
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node.left.value)
        print(node.value)
        if self.right:
            self.right.in_order_print(node.right.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
