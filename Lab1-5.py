#Lab1.5 Recursion List Sum
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
print( recursive_list_sum([2, 4, [6,8],[10,12]]))

