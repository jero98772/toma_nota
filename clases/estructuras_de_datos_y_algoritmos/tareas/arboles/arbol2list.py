class node:
	def __init__(self,data,rigth=None,left=None):
		self.data=data
		self.rigth=rigth
		self.left=left
def tolist(root,tmp,arr=[]):
	try:
		print(root.data)
	except:
		pass
	if not root :
		return tmp
	if not root.left:
		tmp=tolist(root.left,tmp,arr)
	if not root.rigth: 
		tmp=tolist(root.rigth,tmp,arr)
	return tmp
	arr.append(root.data)



class TreeNode:
    def __init__(self, value, isLeaf):
        self.left = None
        self.right = None
        self.value = value
        self.isLeaf = isLeaf

        
def breadth_first(t):
    q = [t]
    while q:
        current = q.pop(0)
        yield current.value if current else None
        if current and not current.isLeaf:
            q.extend([current.left, current.right])
        
            
if __name__ == '__main__':
	t = TreeNode(5, False)
	t.left = TreeNode(4, False)
	t.right = TreeNode(7,False)
	t.left.rigth = TreeNode(3, False)
	t.left.left = TreeNode(2, False)
	t.left.rigth.left=TreeNode(1, True)
	t.left.left.left = TreeNode(0, True)
	t.right.right = TreeNode(8,True)

	print(list(breadth_first(t)))
"""
    root = node(5)
    root.left = node(4)
    root.left.left = node(2)
    root.left.rigth = node(3)
    root.left.left.left = node(1)
    root.right = node(7)
    root.right.right = node(8)
    lst=[]
    tolist(root,lst)
    print(lst)
"""
