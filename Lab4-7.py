# Positional list implemented with doubly linked list data strcuture

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

#------ Lab4.7 Positional list implemented with doubly linked list data strcuture -------------------

class PositionalList(_DoublyLinkedBase):   # inherited from _DoublyLinkedBase
    """A sequential container of elements allowing positional access."""
    
    # -------------- nested Position class --------------- #
    class Position:
        """An absrtraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container  # reference to the list instance that contains the specified node
            self._node = node
            # ** With the container reference, we can roubstly detect when a caller 
            # sends a position instance that does not belong to the indicated list.
        
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not representing the same location."""
            return not (self == other)   # oppositie of __eq__
    
    # -------------------- utility methods -------------------- #
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        # verify if the Position belong to this list
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:    # `None`: convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        """Return Position instance for given node. (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None                       # boundary violation
        else:
            return self.Position(self, node)  # legitimate position
    
    # ------------------------ accessor ------------------------ #
    def first(self):
        """Return the first Position in the list (or NOne if list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def __str__(self):
        """String representation of PositionalList."""
        return str([e for e in self])
    
    # ----------------------- mutator ---------------------- #
    
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between exisitng nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert elelment e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)   # inherited method returns element
    
    def replace(self, p , e):
        """Replace the element at Position p with e.
        
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element        # temporarily store old element
        original._element = e                # replace with new element
        return old_value                     # return the old element value

# Testing PostionalList
L = PositionalList()
print(L)

[L.add_first(i) for i in range(5, 0, -1)]
print(L)
[L.add_last(i) for i in range(6, 11)]
print(L)

first = L.first()
second = L.after(first)
last = L.last()
second_last = L.before(last)
print('First:', first.element())
print(L.before(first))
print('Last:', last.element())
print('After first:', second.element())
print('Before last:', second_last.element())

L.add_after(second, 2.5)
L.add_before(second_last, 8.5)
print(L)

L.delete(second_last)
L.replace(second, -100)
print(L)
