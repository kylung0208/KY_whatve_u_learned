def func1(list):
	print(f"[func1] lst1 = {list}, id = {id(list)}")
	list = [9, 11]
	print(f"[func1] lst1 = {list}, id = {id(list)}")

def func2(list):
	print(f"[func2] lst2 = {list}, id = {id(list)}")
	list += [9, 11]
	list.append(50)
	list.extend([60,70])
	print(f"[func2] lst2 = {list}, id = {id(list)}")

def func3(list):
	print(f"[func3] lst3 = {list}, id = {id(list)}")
	list = list + [9, 11]
	print(f"[func3] lst3 = {list}, id = {id(list)}")

if __name__ == '__main__':
	lst1 = [1,3,5,7]
	lst2 = [1,3,5,7]
	lst3 = [1,3,5,7]

	print(f"[main (before)] lst1 = {lst1}, id = {id(lst1)}")
	print(f"[main (before)] lst2 = {lst2}, id = {id(lst2)}")
	print(f"[main (before)] lst3 = {lst3}, id = {id(lst3)}")

	func1(lst1)
	func2(lst2)
	func3(lst3)

	print(f"[main (after)] lst1 = {lst1}, id = {id(lst1)}")
	print(f"[main (after)] lst2 = {lst2}, id = {id(lst2)}")
	print(f"[main (after)] lst3 = {lst3}, id = {id(lst3)}")

	"""
	[main (before)] lst1 = [1, 3, 5, 7], id = 4331219784
	[main (before)] lst2 = [1, 3, 5, 7], id = 4331219848
	[main (before)] lst3 = [1, 3, 5, 7], id = 4331264264
	[func1] lst1 = [1, 3, 5, 7], id = 4331219784
	[func1] lst1 = [9, 11], id = 4331264200
	[func2] lst2 = [1, 3, 5, 7], id = 4331219848
	[func2] lst2 = [1, 3, 5, 7, 9, 11, 50, 60, 70], id = 4331219848
	[func3] lst3 = [1, 3, 5, 7], id = 4331264264
	[func3] lst3 = [1, 3, 5, 7, 9, 11], id = 4331264136
	[main (after)] lst1 = [1, 3, 5, 7], id = 4331219784
	[main (after)] lst2 = [1, 3, 5, 7, 9, 11, 50, 60, 70], id = 4331219848
	[main (after)] lst3 = [1, 3, 5, 7], id = 4331264264
	"""