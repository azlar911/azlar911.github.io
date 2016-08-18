class rectangle:
	def __init__(self, width, length):
		self.w = width
		self.l = length
		
	def calArea(self):
		return self.w * self.l
	def calPeri(self):
		return 2*(self.w + self.l)
		
	