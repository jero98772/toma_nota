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
    def getData(self):
        data=""
        current=self.headx
        while current.next:
            data+=" "+str(current.val)
            current=current.next
        current.next=newNode

    def search(self, itemsearch):
        current=self.head
        while current != None:
            if current.val == itemsearch:
                return current 
             
            current = current.next
         
        return False

 
 
def recSearch(node,itemsearch):
    current=node
    if not current:
        return -1#not found
    else:
        if current.val==itemsearch:
            return current
        else:
            return recSearch(current.next,itemsearch)

def recPos(node,itemsearch,pos):
    current=node
    if not current:
        return -1#not found
    else:
        if current.val==itemsearch:
            return pos
        else:
            return recPos(current.next,itemsearch,pos+1)

def recInsert(node,item,pos,posobj):
    current=node
    if not current:
        return -1#not found
    else:
        if pos==posobj:
            return pos
        else:
            return recPos(current.next,item,,pos+1)

def max(node,maxnum):
    current=node
    if not current:
        return -1#not found
    else:
        if maxnum<current.val:
            return recSearch(current.next,itemsearch,current.val)
        else:
            return recSearch(current.next,itemsearch,maxnum)

def test():
    ll=linkedList()
    ll.madd(1,2,3,6,5,7,8,4)
    #print(ll.search(4).val)
    #tmp=recSearch(ll.head,4)
    #print(tmp.val)
    print(recPos(ll.head,4,0))
    print(recInsert(ll.head,4,3,0))


test()