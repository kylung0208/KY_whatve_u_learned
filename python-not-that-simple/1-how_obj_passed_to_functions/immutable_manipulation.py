def str_manipulate1(string):
	string += '_manipulated'

def str_manipulate2(string):
	string = string + '_manipulated'

def tuple_manipulate(tup):
	list(tup).append(100)
	tup = tuple(tup)


if __name__ == '__main__':
	string1 = 'ThisIsAString'
	string2 = 'ThisIsAString'
	str_manipulate1(string1)
	str_manipulate2(string2)

	print(f"[manipulated] string1 = {string1}")
	print(f"[manipulated] string2 = {string2}")

	"""
	! String cannot be manipulated (in place), therefore, one cannot manipulated a string in a function.
	! immutable object like string would act like `pass by value` in python.

	[manipulated] string1 = ThisIsAString
	[manipulated] string2 = ThisIsAString
	"""

	tup = (1,2,3)
	tuple_manipulate(tup)
	print(f"tup = {tup}")
	"""
	! Also tuple, you can't add elements to a tuple because of their immutable property.
	! There is no append() or extend() method for tuples.
	! You cannot remove elements from a tuple, also because of their immutability.
	! Tuples have no remove() or pop() method.

	tup = (1, 2, 3)
	"""