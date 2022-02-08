def main():
	mana=0
	minMana=0
	n=int(input())
	a=input().split(" ")
	for i in range(n):
		mana+=int(a[i])
		if mana<0 and int(a[i])!=0:
			print("aqui")
			minMana+=mana
	print(minMana*-1)
main()