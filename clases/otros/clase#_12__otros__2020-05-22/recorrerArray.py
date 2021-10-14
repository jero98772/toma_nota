list1=[1,2,2,333,3,3,3333,44,4,4,444,5]
def listIndex(i):
	print(i,list1[i-1])
	if i>len(list1)-1:return 
	else: listIndex(i+1) ;return
listIndex(0)

"""
list1=[1,2,2,333,3,3,3333,44,4,4,444,5]
def listIndex(i):
	print(i,list1[-i-1])
	if i < 1:return 
	else: listIndex(i-1) ;return
listIndex(len(list1)-1)
"""