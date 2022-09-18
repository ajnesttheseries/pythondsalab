#Lab1.4 The sum of a list of numbers
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print(list_sum([3, 6, 9, 12, 16]))

