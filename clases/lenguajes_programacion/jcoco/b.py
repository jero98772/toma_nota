import dis

def main():
	a=int(input())
	if a%2==0:
		for i in range(0,a,2):
			print(i)
	else:
		i=1
		while i<=a:
			print(i)
			i+=2
#main()
dis.dis(main)
