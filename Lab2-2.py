import ctypes 
class DynamicArray(object): 
    """DYNAMIC ARRAY CLASS (Similar to Python List)"""
    #initilize ir
    def __init__(self):
        #We will have 3 atributes
        self.n = 0 # Count actual elements (Default is 0) 
        self.capacity = 1 # Default Capacity 
        self.A = self.make_array(self.capacity) #make_array will be defined later
    #special len method    
    def __len__(self):
        """Return number of elements sorted in array""" 
        return self.n      
    def __getitem__(self, k): 
        """Return element at index k"""
        if not 0 <= k <self.n: 
            # Check it k index is in bounds of array 
            return IndexError('K is out of bounds !')      
        return self.A[k] # Retrieve from the array at index k          
    def append(self, ele): 
        """Add element to end of the array"""
        #Checking the capacity
        if self.n == self.capacity: 
            # Double capacity if not enough room 
            self._resize(2 * self.capacity)     #_resize is the method that is defined later
        #Set the n indexs of array A to element
        self.A[self.n] = ele  
        self.n += 1        
    def _resize(self, new_cap): #new_cap is for new capacity 
        """Resize internal array to capacity new_cap"""
        #Decalare array B
        B = self.make_array(new_cap)    
        for k in range(self.n): # Reference all existing values 
            B[k] = self.A[k]       
        self.A = B # Call A the new bigger array 
        self.capacity = new_cap # Reset the capacity
    #making the make-array method using ctypes
    def make_array(self, new_cap): 
        """Returns a new array with new_cap capacity"""
        return (new_cap * ctypes.py_object)() 
