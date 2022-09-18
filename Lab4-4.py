#Circularly Linked Lists
class CircularQueue:
    """Queue implementation using circularly linked list for storage."""
    
    # ------------------------------------ #
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'   
        
        def __init__(self, e, next_):     
            self._element = e             
            self._next = next_ 
    
    # ------------------------------------ #
    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        self._size -= 1
        if self._size == 0:      # removing only element
            self._tail = None    # queue becomes empty
        else:
            self._tail._next = oldhead._next # bypass the  old head
        return oldhead._element
    
    def enqueue(self, e):
        """Add an element e to the back of queue."""
        newest = self._Node(e, None)          # new tail node
        # ***
        if self.is_empty():
            newest._next = newest             # initialize circularly
        else:
            newest._next = self._tail._next   # new tail node points to head
            self._tail._next = newest         # old tail node points to new node         
        self._tail = newest                   # new node becomes the tail
        self._size += 1
        
    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next     # old head becomes new tail
            
    def __str__(self):
        """String representation of the stack."""
        expr = []
        if self.is_empty():
            return "[]"
        current = self._tail._next     # set current to `head` node
        expr.append(current._element)
        # while not circular back to head
        while current._next != self._tail._next:
            current = current._next
            expr.append(current._element)
        return str(expr)

Q = CircularQueue()
print(Q)

Q.enqueue("LAX")
Q.enqueue("MPS")
print(Q)

Q.dequeue()
print(Q)

Q.enqueue("ATL")
print('First: ', Q.first())

Q.enqueue("BOS")
print(Q)

Q.rotate()
print(Q)
