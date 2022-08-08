#se uso codigo de roseta code para merge sort
import random
def genrandom(n):
	randomlist = []
	for i in range(n):
		n = random.randint(0,100000)
		randomlist.append(n)
	return randomlist
a=genrandom(2000000)
print(a)
import sys
print(sys.getsizeof(a))
from heapq import merge
 
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
print(merge_sort(a))