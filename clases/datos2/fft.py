from cmath import exp
pi=3.141592653589793238462

def fft(x):
	N=len(x)
	if N<=1:return x
	m=fft(x[0::2])
	M=fft(x[1::2])
	exprecion=[exp(-2j*pi*k/N)]