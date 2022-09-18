#Implementing a Deque with a Doubly Linked List
#--------------------- Inherite Class #DoublyLinkedBase of Lab 4.5
class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""
    
    # ------------ nested Node class ---------- #
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next_):
            self._element = element
            self._prev = prev         # previous node reference
            self._next = next_        # next node reference
    
    # -------------- doubly linked base methods ----------- #
    def __init__(self):
        """Create an emtpy list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, self._header, None)  # header is before trailer
        self._header._next = self._trailer                    # trailer is after header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element        # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element                 # return deleted element
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        expr = []
        current = self._header
        while current._next != self._trailer:
            current = current._next
            expr.append(current._element)
        return str(expr)

#----------------------------- Linked Deque --------------------------------
class LinkedDeque(_DoublyLinkedBase):  # inherite from _DoublyLinkedBase
    """Double-ended queue implementation based on a doubly linked list."""
    
    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        first_node = self._header._next
        return first_node._element      # first node after the header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        last_node = self._trailer._prev
        return last_node._element       # last node before the trailer
    
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        # use inherited method
        self._insert_between(e, self._header, self._header._next)   # insert after header
    
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # insert before trailer
        
    def delete_first(self):
        """Remove and return the element from the front of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        # use inherited method
        self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element from the back of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._trailer._prev)

Q = LinkedDeque()
print(Q)

[Q.insert_first(i) for i in range(5, 0, -1)]
print(Q)

[Q.insert_last(i) for i in range(6, 11)]
print(Q)

Q.delete_last()
print(Q)
Q.delete_first()
print(Q)

