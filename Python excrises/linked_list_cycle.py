class listNode():
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next



def hasCycle(head):
    dummy =  head
    slow = fast = dummy

    while slow != fast:
        if not fast or fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

node1 = listNode(3)
node2 = listNode(2)
node3 = listNode(0)
node4 = listNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2        

print(hasCycle(node1))