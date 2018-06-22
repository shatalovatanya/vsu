list = ['s', 'e', 'e', 'y', 'o', 'u', 's', 'p', 'a', 'c', 'e', 'c', 'o', 'w', 'b', 'o', 'y']
searchSymb = input('Введите искомый символ: ')
print(list.index(searchSymb))
def lineSearch(list, x):
	result = None
	for index, string in enumerate(list):
		print(index, string)
		if string == x:
			result = index
	return result