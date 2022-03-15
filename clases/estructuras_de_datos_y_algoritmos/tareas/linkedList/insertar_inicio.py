class Node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

def insertarAlInicio(head: Node,values:list) -> Node:
    newN=Node(6)
    newN.next=head
    head=newN
    return head