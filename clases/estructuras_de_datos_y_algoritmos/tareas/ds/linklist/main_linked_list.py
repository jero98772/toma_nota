class node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    def add(self,data):
        newNode=node(data)
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
def recSearch(head,k,pos):
    if not head.next:
        return -1#not found
    if head.value==k:
        return pos
    else:
        head=head.next
        recSearch(head,k,pos+1)

def test():
    ll=linkedList()
    ll.madd(1,2,4,5)
test()