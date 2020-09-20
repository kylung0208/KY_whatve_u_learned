class Foo:
	def __init__(self):
		self.bar = 1
		self.num = 1
		self.word1 = 'a'
		self.word2 = 'a'

def class_manipulation1(x):
	x.bar += 1
	x.num = x.num + 1
	x.word1 += 'b'
	x.word2 = 'b'

def class_manipulation2(x):
	new_foo = Foo()
	x = new_foo
	x.bar += 1
	x.num = x.num + 1
	x.word1 += 'b'
	x.word2 = 'b'

if __name__ == '__main__':
	# example 1
	foo1 = Foo()
	class_manipulation1(foo1)

	print(f"foo1.bar = {foo1.bar}")
	print(f"foo1.num = {foo1.num}")
	print(f"foo1.word1 = {foo1.word1}")
	print(f"foo1.word2 = {foo1.word2}")

	"""
	foo1.bar = 2
	foo1.num = 2
	foo1.word1 = ab
	foo1.word2 = b
	"""
	#------------------------------------------------------
	# example 2
	foo2 = Foo()
	class_manipulation2(foo2)

	print(f"foo2.bar = {foo2.bar}")
	print(f"foo2.num = {foo2.num}")
	print(f"foo2.word1 = {foo2.word1}")
	print(f"foo2.word2 = {foo2.word2}")

	"""
	foo2.bar = 1
	foo2.num = 1
	foo2.word1 = a
	foo2.word2 = a
	"""

