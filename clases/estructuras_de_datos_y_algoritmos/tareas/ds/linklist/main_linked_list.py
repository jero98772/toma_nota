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
        current=self.head
        while current.next:
            data+=" "+str(current.val)
            current=current.next
        return data
        #current.next=newNode

    def search(self, itemsearch):
        current=self.head
        while current != None:
            if current.val == itemsearch:
                return current 
             
            current = current.next
         
        return False
    def insert(self, x, data):
        n = self.head
        print(n.next)
        while not n :
            if n.val == x:
                break
            n = n.ref
        if not n :
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
 
 
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

def recInsert(head,node,item:node,posobj,pos):
    #print(posobj,pos)
    current=node
    if not current:
        return -1#not found
    else:
        if pos==posobj:
            tmp=current.next
            item.next=tmp
            current.next=item   
            return head  
        elif posobj==0:
             item.next=head
        else:
            return recInsert(head,current.next,item,posobj,pos+1)

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
    ll.madd(1,2,3,6,5,7,8)
    #print(ll.search(4).val)
    #tmp=recSearch(ll.head,4)
    #print(tmp.val)
    #print(recPos(ll.head,4,0))
    recInsert(ll.head,ll.head,node(4),0,0)
    recInsert(ll.head,ll.head,node(4),0,0)
    recInsert(ll.head,ll.head,node(4),0,0)

    print(ll.getData())


test()