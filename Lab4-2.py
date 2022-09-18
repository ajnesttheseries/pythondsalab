#Implement a Stack with a Singly Linked List
class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    
    # ------------- nested _Node class ------------- #
    class _Node:
        """Lightweight nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'   # streamline memory usage
        
        def __init__(self, e, next_):     # initialize node's field
            self._element = e             # reference to use's element
            self._next = next_            # reference to next node

    # -------------- stack methods --------------- #
    def __init__(self):
        """Create an empty stack."""
        self._head = None                 # reference to the head node
        self._size = 0                    # number of stack elements
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element         # top of stack is at the head of list
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)  # create and link to a new node
        self._size += 1
        
    def pop(self):
        """Remove and return the element from the top of the stack (LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next      # bypass the former top node
        self._size -= 1
        return answer
    
    def __str__(self):
        """String representation of the stack."""
        expr = []
        if self.is_empty():
            return "[]"
        current = self._head
        expr.append(current._element)
        while current._next != None:
            current = current._next
            expr.append(current._element)
        return str(expr)


S = LinkedStack()
print(S)

S.push("BOS")
S.push("ATL")
print(S)

S.push("MPS")
S.push("LAX")
print(S)

S.pop()
S.pop()
print(S)
