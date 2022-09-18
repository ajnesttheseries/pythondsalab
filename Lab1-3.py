#Lab1.3 Binary Search Algorithm
def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive."""
    if low > high:
        return False                #interval is empty; no match
    else:
        mid = (low + high)//2
        if target == data[mid]:     #found a match
            return True
        elif target < data[mid]:
            #return on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            #recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)

data = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]        
print(binary_search(data, 37, 0, len(data)-1))
print(binary_search(data, 10, 0, len(data)-1))
print(binary_search(data, 7, 0, len(data)-1))
print(binary_search(data, 9, 0, len(data)-1))
print(binary_search(data, 20, 0, len(data)-1))
print(binary_search(data, 13, 0, len(data)-1))


