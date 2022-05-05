class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BuscarBST(root,val):
    if (nodeExists(root, val)):
        return "YES"
    else:
        return "NO"
        
def nodeExists(node, val):
    if (node == None):
        return False
    elif (node.val == val):
        return True
    #siga buscando en el lado izquierod
    if nodeExists(node.left, val):
        return True
    #busque en el lado derecho
    return nodeExists(node.right, val)
 