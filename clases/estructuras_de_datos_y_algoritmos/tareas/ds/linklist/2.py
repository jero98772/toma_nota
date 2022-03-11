class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(head1: Node, head2: Node) -> Node:
    # Aquí va el codigo.
    # Retorna la cabeza de la lista
    tmp = node(0)
    tail=tmp
    while True:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    return tmp