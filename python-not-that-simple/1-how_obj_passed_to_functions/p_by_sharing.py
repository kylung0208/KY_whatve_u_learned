def change_x(x):
	print(f"[func (before)] x = {x}, id = {id(x)}")
	x = 42
	print(f"[func (after)] x = {x}, id = {id(x)}")

if __name__ == '__main__':
	x = 9
	print(f"[main (before)] x = {x}, id = {id(x)}")
	change_x(x)
	print(f"[main (after)] x = {x}, id = {id(x)}")

	"""
	[main (before)] x = 9, id = 4305283712
	[func (before)] x = 9, id = 4305283712
	[func (after)] x = 42, id = 4305284768
	[main (after)] x = 9, id = 4305283712
	"""