from sys import argv

class myclass:
	"""
	123456789
	222222
	"""

	def __init__(self, argvIn):
		self.wallet = argvIn

	def punIn(self, num):
		self.wallet += num
		
	def takeOut(self, num):
		self.wallet -= num
		
	def __str__(self):
		return str(self.wallet)
		
		

wal = myclass(int(argv[1]))
print(wal.__doc__)
a = input("In: ")
wal.punIn(int(a))
print(wal)

a = input("Out: ")
wal.takeOut(int(a))
print(wal)