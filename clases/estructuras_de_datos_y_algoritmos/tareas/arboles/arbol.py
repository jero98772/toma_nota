class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TamañoArbol(root):
    irdaux(root,0)
    print(root.val)
def irdaux(tree,count):
	if not tree.right:
	     irdaux(tree.right,count+1)
	if not tree.left:
	     irdaux(tree.left,count+1)
	else: return count     
	"""if not tree.left:
	    return ird(tree.right,count+1) 
	else:
		return ird(tree.left,count+1)"""