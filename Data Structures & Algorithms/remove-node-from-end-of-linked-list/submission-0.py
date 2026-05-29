# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach 
        # create dummy node
        # p1, p2 = dummy
        # move p1 n spaces ahead
        # now move p1 & p2 together until p2.next is null
        # now remove connection of p1.next and merge with p1.next.next

        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy

        for i in range(n):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return dummy.next