from Lab5_2_BinaryTree import BinaryTree
class ArrayBinaryTree(BinaryTree):
    """Array-based representation of a binary tree structure."""
    
    # --------------- binary tree constructor ---------------- #
    def __init__(self):
        """Create an initially empty binary tree."""
        self._container = [None]  # python list to store elements, root is initialize to `None`
        self._size = 0
    
    def _extend_container(self, depth):
        """Extend internal array by 2**height."""
        next_level = [None] * (2**depth)
        self._container.extend(next_level)
        
    # ------------------ public accessor --------------------- #
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def root(self):
        """Return the root Postion of the tree (or None if tree is empty)."""
        return None if self.is_empty() else 0
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        if p == 0:          # root 
            return None
        if p % 2 == 1:      # left child
            return (p-1)/2
        else:               # right child
            return (p-2)/2
    
    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        if len(self._container) < 2**(self.depth(p)+1):  # next level does not exist
            return None
        return 2*p + 1
    
    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        if len(self._container) < 2**(self.depth(p)+1):  # next level does not exist
            return None
        return 2*p + 2
    
    def element(self, p):
        """Return the element at Position p."""
        if p+1 > len(self._container):    # position p does not exist
            return None
        return self._container[int(p)]
    
    def num_children(self, p):
        """Return the number fo children of Position p."""
        count = 0
        # if left child exists (index is not out of range and element exists)
        if (2*p + 1)+1 <= len(self._container) and self._container[2*p + 1] is not None:
            count += 1
        # if right child exists
        if (2*p + 2)+1 <= len(self._container) and self._container[2*p + 2] is not None:   
            count += 1
        return count
    
    # --------------- nonpublic update methods ---------------- #
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        
        Raise ValueError if tree nonempty.
        """
        if self._container[0] is not None: raise ValueError('Root exists')
        self._size = 1
        self._container[0] = e
        return 0
    
    def _add_left(self, p, e):
        """Store element e in the left child for Position p.
        
        Return the Position of new left child.
        Raise ValueError if Position p invalid or p already has a left child.
        """
        if (2*p+1) + 1 > len(self._container):      # container does not have enough space
            self._extend_container(self.depth(p)+1) # extend container
        if self._container[2*p + 1] is not None: raise ValueError('Left child exists')
        self._container[2*p + 1]  = e   # left child
        self._size += 1
        return (2*p + 1)
    
    def _add_right(self, p, e):
        """Store element e in the right child for Position p.
        
        Return the Position of new right child.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        if (2*p+2) + 1 > len(self._container):      # container does not have enough space
            self._extend_container(self.depth(p)+1) # extend container
        if self._container[2*p + 2] is not None: raise ValueError('Right child exists')
        self._container[2*p + 2] = e  # right child
        self._size += 1
        return (2*p + 2)
    
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        old_element = self._container[p]
        self._container[p] = e
        return old_element
