class Point:
	def __init__(self, other, x = 0, y = 0):
		self.x = x
		self.y = y
	def  __str__(self):
		return str(self.x) + str(self.y)
	def __lt__(self, other):
		return Point(self.x < other.x or self.x == other.x and self.y < other.y)
	def __add__(self, other):
		return Point(self.x + other.x , self.y + other.y)
	def __sub__(self, other):
		return Point(self.x - other.x , self.y - other.y)
	def __mul__(self, other):
		return Point(self.x * other.x , self.y * other.y)
	def __truediv__(self, other):
		return Point(self.x / other.x , self.y / other.y)
	def __dosmth__(self):
		return Point(self.x **2 + self.y**2) 
		
  n=int(input())
  max=None
  for i in range(N):
	  A=Point(input())
    if max==None or A.__dosmth__()>max.__dosmth__():
	    max=A
  print(max)
