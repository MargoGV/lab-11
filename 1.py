class Point:
	def __init__(self, st='0,0',ms=1):
		self.x = float(st[:st.index(,)])
		self.y = float(st[st.index(,)+1:]
		sels.ms=ms
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
n=int(input())
for i in range(0,n):
	x=int(input())
	y=int(input())
	a=Point(x,y)
	c = x + y
print(c)
