# Implementation of Singly Linked List
class SinglyLinkedList:
    """Singly linked list implementation using object `Node` for storage."""
    
    # ---------- Nested _Node class ---------- #
    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next'      # streamline memory usage
        
        # initialize node's fields, 
        # use `next_` to avoid conflic with the built-in function `next`
        def __init__(self, element, next_):
            self._element = element          # reference to user's element
            self._next = next_               # reference to next node
    
    # ----------- linked list methods ----------- #
    def __init__(self):
        """Create an empty list."""
        self._head = None   # reference to the head node
        self._tail = None   # reference to the tail node
        self._size = 0      # number of stack elements
    
    def __len__(self):
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0
    
    def add_first(self, e):
        """Insert an element at the beginning of the linked list."""
        newest = self._Node(e, self._head)  # create new node instance
        if self.is_empty():            # if the list is originally empty
            self._tail = newest        # make `_tail` to point to `newest` as well
        self._head = newest            # make `_head` to point to `newest`
        self._size += 1
    
    def add_last(self, e):
        """Insert an element at the end of the linked list."""
        newest = self._Node(e, None)
        if self.is_empty():            # if the list is originally empty
            self._head = newest        # make `_head` point to `newest`
        else:                          # if not originally empty
            self._tail._next = newest  # make old tail node to link to newset
        self._tail = newest            # make `newest` the new `_tail` node
        self._size += 1
        
    def remove_first(self):
        """Remove the node at the beginning of the linked list."""
        if self.is_empty():
            raise Empty('Linked list is empty')
        self._head = self._head._next   # make `_head` point to the next node (or None)
        self._size -= 1
        
    def remove_last(self):
        """Remove the node at the end of the linked list."""
        if self.is_empty():
            raise Empty('Linked list is empty')
        new_last = self._traverse(self._size-1)   # find the second to last node
        self._tail = new_last                    # make `_tail` point to the new last node
        self._tail._next = None                  # make the new last node point to None 
        
    def _traverse(self, n):
        """Traverse the linked n steps from `_head` and reutrn the node."""
        current = self._head
        for _ in range(1, n):
            current = current._next
        return current

    def __str__(self):
        """Return string representation of the linked list."""
        expr = []
        if self.is_empty():
            return "[]"
        current = self._head
        expr.append(current._element)
        while current._next != None:
            current = current._next
            expr.append(current._element)
        return str(expr)

S = SinglyLinkedList()
print(S)

S.add_first("MSP")
print(S)
S.add_last("ATL")
print(S)
S.add_first("LAX")
print(S)
S.add_last("BOS")
print(S)
S.remove_first()
S.remove_last()
print(S)
