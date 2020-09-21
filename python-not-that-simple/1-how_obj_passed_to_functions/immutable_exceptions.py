
def change_list_content_in_tuple(a):
	a[1].append(4)

if __name__ == '__main__':
	a = ("foobar", [1,2,3])
	print(f"id(a[0])={id(a[0])}, id(a[1])={id(a[1])}")
	change_list_content_in_tuple(a)
	print(a)
	print(f"id(a[0])={id(a[0])}, id(a[1])={id(a[1])}")
	
