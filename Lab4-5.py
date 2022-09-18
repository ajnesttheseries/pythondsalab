#Doubly Linked Lists
# A base class for managing a doubly linked list

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

L = _DoublyLinkedBase()
print(L)
L._insert_between(0, L._header, L._trailer)
print(L)
L._insert_between(1, L._header._next, L._trailer)
print(L)
L._delete_node(L._header._next)
print(L)
