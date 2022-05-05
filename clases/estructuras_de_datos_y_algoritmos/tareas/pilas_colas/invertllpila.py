class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def add(self,data):
        newNode=Node(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    def madd(self,*data):
        for i in data:
            newNode=node(i)
            if self.head:
                current=self.head
                while current.next:
                    current=current.next
                current.next=newNode
            else:
                self.head=newNode
def invertir(head: Node) -> Node:
    from collections import deque
    current=head
    q=deque()
    while current != None:
        q.append(current.val)
        current = current.next
    q.reverse() 
    ll=linkedList()
    for i in range(len(q)):
        ll.add(q.pop())
    return ll.head

    