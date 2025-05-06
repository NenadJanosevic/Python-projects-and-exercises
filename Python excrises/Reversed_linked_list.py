class ListNode:
    def __init__(self,val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution(object):
    def reveseList(self,head:ListNode):
        cur = head
        prev = None
        while cur:
            new_cur = cur.next
            cur.next = prev
            prev = cur
            cur = new_cur
        return prev
        



head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
x = s.reveseList(head1)
current = x
while current:
    print(current.val)
    current = current.next