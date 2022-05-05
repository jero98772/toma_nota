class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ArbolesIguales(root1,root2):
    if not root1 and not root2:
        return True
    elif not root1 and not root2 :
        return ((root1.data == root2.data) and
                identicalTrees(root1.left, root2.left)and
                identicalTrees(root1.right, root2.right))
    return False