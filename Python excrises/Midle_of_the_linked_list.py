class ListNode(object):
    def __init__(self,data = 0,next = None):
        self.data = data
        self.next = next
class Solution(object):
    @staticmethod
    def middleNode(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
class creatLinkedList(object):
    def __init__(self):
        self.head = None

    def appendMethod(self,data):
        new_nood = ListNode(data)
        if self.head is None:
            self.head = new_nood
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_nood



my_list = creatLinkedList()
my_list.appendMethod(1)
my_list.appendMethod(2)
my_list.appendMethod(3)
my_list.appendMethod(4)
my_list.appendMethod(5)

sol = Solution()
middle = sol.middleNode(my_list.head)
print("Middle Node Data:", middle.data)

            
    

