class node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

class linkedList:
	def __init__(self):
        self.head = None
    def insert(node):
        self.next
    def add_first(self, node):
        node.next = self.head
        self.head = node

|
def insertarAlInicio(head: Node, allList:Node) -> Node:
    return head.next(allList)
def main():
    values=[1,23,46,8,3,1] 
    tmp=True
    n=Node(values[0])
    nn=Node(values[1])
    nnn=Node(values[2])
    n.next=nn
    nn.next=nnn

    for i in values[1:]:
        newNode=Node(i)
        if tmp:
            n.next=newNode
            tmp=False
        else:
            newNode=Node(i)
            newNode.next(newNode)

main()