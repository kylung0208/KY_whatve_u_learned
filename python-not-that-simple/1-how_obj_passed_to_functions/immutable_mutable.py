if __name__ == '__main__':
	"""
	Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
	[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> a = 5
	>>> id(a)
	4305283584
	>>> b = 5
	>>> id(b)
	4305283584
	>>> a is b
	True
	>>> a = [1,2,3]
	>>> id(a)
	4333226888
	>>> b = [1,2,3]
	>>> id(b)
	4333271944
	>>> a = (1,2,3)
	>>> id(a)
	4333244848
	>>> b = (1,2,3)
	>>> id(b)
	4333245208
	>>> a = 'abc'
	>>> b = "abc"
	>>> id(a)
	4331188384
	>>> id(b)
	4331188384
	>>> a = (1,2,3)
	>>> b = (1,2,3)
	>>> a is b
	False
	>>> a = b = (1,2,3)
	>>> a is b
	True
	>>> b = a
	>>> a is b
	True
	>>> id(b)
	4333245280
	>>> id(a)
	4333245280
	>>> a = (1,2,[1])
	>>> a[2]
	[1]
	>>> a[2].append(3)
	>>> a
	(1, 2, [1, 3])
	"""
	pass