import numpy
def detIs0(matrix):
	mDet= np.linalg.det(matrix)
	if mDet != 0:
		return True
	else:
		return False
def det(matrix):
	mDet= np.linalg.det(matrix)
def getAscii128List():
	asciiStr = ""
	for i in range(32,127):
		asciiStr += chr(i)
	return asciiStr
def getAscii128Str():
	asciiList = []
	for i in range(32,127):
		asciiList.append(chr(i))
	return asciiList
class hill():
	def __init__(self,matrix):
		self.matrix = matrix
	def cifrate(self):
		pass
	def descifrate(self):
		pass
print(getAscii128Str())
print(getAscii128List())