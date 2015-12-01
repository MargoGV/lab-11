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
	def TriP(self,other,smth):
	  return self.russt(other)+self.russt(smth)+ other.russt(smth)
	def TriS(self,smth):
	p=self.TriP(other,smth)/2
	b=self.russt(other)
	c=self.russt(smth)
	c=other.russt(smth)
	return (p*(p-a)*(p-b)*(p-c))**0.5

N=int(input())
A=[]
max=None
B=[Point()]*3
for i in range(N):
  A.append(Point(input())
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if max==None or max<A[i].TriS(A[j],A[k]):
      B[0],B[1],B[2]=A[i],A[j],A[k]
      max=A[i].TriS(A[j],A[k])
print(*B)
