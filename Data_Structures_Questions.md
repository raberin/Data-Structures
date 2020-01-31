Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    O(1) since you're appending at the end

2. What is the runtime complexity of `dequeue`?
    O(1) in DLL's due to the nature of the data stucture. Remove the head, change pointers.
3. What is the runtime complexity of `len`?
    Depends entirely on how it's implemented. If it's not saved on constructor, it would be O(n). If it IS saved it's O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    O(n) since it would need to traverse the list and then insert. Typically, it is O(1) operation since there's no shift
2. What is the runtime complexity of `ListNode.insert_before`?
    O(n) since it would need to traverse the list and then insert. Typically, it is O(1) operation since there's no shift
3. What is the runtime complexity of `ListNode.delete`?
    O(n) since it would need to traverse the list and then delete

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(1) since it has a pointer to the head

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(1) since it has a pointer to the head and can move pointers to the next value
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(1) since there's a pointer to tail as well
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(1) since there's a pointer to tail and can easily change pointers
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    Given the node, it would be O(1) to remove it from its current spot and adding to head
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    Given the node, it would be O(1) to remove it from its current spot and adding to tail
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1) since we're not shifting any values. Just chaning pointers?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Any Linked List Delete will beat Array.splice due to the fact that LL's dont need to shift values during a deletion. A linked list just needs to change pointers to skip the node, while in an array it must be removed and every value after must be shift over to the left. 