def main():
	mana=0
	minMana=0
	n=int(input())
	a=input().split(" ")
	for i in range(n):
		mana+=int(a[i])
		print("")
		if mana<http://codeforces.com/gym/102569<0:
			minMana=mana
	print(minMana*-1)
main()