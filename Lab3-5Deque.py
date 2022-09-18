
class ArrayDeque:
    def __init__(self):
        INIT_CAP = 10
        self._data = [None]*INIT_CAP
        self._n = 0
       # self._first = 0
       # self._last = 0
        
    def __len__(self):
        """length of deque"""
        return self._n

    def __str__(self):
        """string representation of deque"""
        return str(self._data)

    def is_empty(self):
        """returns true if deque is empty"""
        return self._n==0

    def first(self):
        if self.is_empty():
            raise Empty('Dequee is empty')
        return self._data[self._first]

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._last]


    def add_first(self, e):
        """add item to beginning of deque"""
        if(self._n==len(self._data)):
            self._resize(2*self._n)
        # First minus one because moving one index ahead of first
        addix = (self._first - 1)%len(self._data)
        self._data[addix] = e
        self._first = addix
        self._n += 1

    def add_last(self, e):
        """add item to end of deque"""
        if(self._n==len(self._data)):
            self._resize(2*self._n)
        # First plus n: jumping to the next open index,
        # which must be index first + n.
        # If there are n items starting at first, then they will be
        # at first through (first + n - 1).
        # Next open index is at first + n.
        addix = (self._first + self._n)%(len(self._data))
        self._data[addix] = e
        self._n += 1

    def delete_first(self):
        if(not self.is_empty()):
            ret = self._data[self._first]
            self._data[self._first] = None
            self._first = (self._first + 1)%(len(self._data))
            self._n -= 1

            # If we're down to smaller than a quarter occupied,
            # cut array size in half.
            if(self._n < len(self._data)//4):
                self._resize(len(self._data)//2)

        else:
            raise Empty("oops, empty deque")

    def delete_last(self):
        if(not self.is_empty()):
            getix = (self._first + self._n - 1)%(len(self._data))
            ret = self._data[getix]
            self._data[getix] = None
            self._n -= 1

            # If we're down to smaller than a quarter occupied,
            # cut array size in half.
            if(self._n < len(self._data)//4):
                self._resize(len(self._data)//2)

        else:
            raise Empty("oops, empty deque")

    def _resize(self,newcap):
        """private method: resize the underlying array"""
        old = self._data
        self._data = [None]*newcap
        walk = self._first

        # Need to pay close attention here:
        # range over each of the n elements
        for k in range(self._n):
            self._data[k] = old[walk]
            # Increment walk after the update, not before
            walk += 1
            walk %= len(old)

        self._first = 0
"""
D = ArrayDeque()
D.add_last(5)
D.add_first(3)
D.add_first(7)
print(D.first())
print(D.delete_last())
print(len(D))
print(D.delete_last())
print(D.delete_last())
D.add_first(6)
print(D.last())
D.add_first(8)
print(D.is_empty())
print(D.last())"""
