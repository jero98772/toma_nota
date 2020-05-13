import numpy as np
def mtrixmult(m1,m2):

	m1=np.asarray(m1)
	m2=np.asarray(m2)
	
	M=m1*m2
	return M
M = [ [8,34,22,25,9], [-11,2,4,5,0], [-4,-6,12,50,17] ]
a = [ M[-2][-2:], M[1][:2], M[-1][-4:-2] ]
b = M[-2:]
mtrixmult(a,b)