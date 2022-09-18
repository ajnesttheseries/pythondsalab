#Case Study: Maintaining Access Frequencies

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

#----- Lab4.9 Case Study: Maintaining Access Frequencies -----------------------

class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""
    
    # ----------------- nested _Item class ---------------- #
    class _Item:
        __slots__ = '_value', '_count'
        
        def __init__(self, e):
            self._value = e    # the user's element
            self._count = 0    # access count initially zero
        
    # ------------------ nonpublic utilities --------------- #
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()         # _data is a list of _Item instances
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():                # consider moving
            count = p.element()._count
            walk = self._data.before(p)
            if count > walk.element()._count:       # must shift forward
                while (walk != self._data.first() and 
                       count > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                value = self._data.delete(p)        # delete position p and return its value
                self._data.add_before(walk, value)  # reinsert value
    
    # ------------------- public methods --------------------- #
    def __init__(self):
        """Create an empyt list of favorites."""
        self._data = PositionalList()   # will be list of _Item instances
    
    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0
    
    def __str__(self):
        """String representation of FavoritesList."""
        return str([item._value for item in self._data])
    
    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)                  # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e))  # if new, place at end
        p.element()._count += 1                     # always increment count
        self._move_up(p)                            # move p forward
        
    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)                  # try to locate existing element 
        if p is not None:
            self._data.delete(p)                    # delete if found
        
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value of k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()                    # element of list is _Item
            yield item._value                        # report user's element (value)
            walk = self._data.after(walk)

F = FavoritesList()
print(F)

for i in range(10):
    song = "song" + str(i)
    F.access(song)
print(F)

[F.access("song4") for _ in range(3)]
[F.access("song3") for _ in range(1)]
print(F)

F.remove("song0")
print(F)
for song in F.top(5):
    print(song)

