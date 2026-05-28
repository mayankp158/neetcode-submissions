# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # approach
        # find mid of link list
        # reverse a link list
        # merge both in alternate fashion

        # find mid of link list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        # reverse a link list
        prev = None       
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            

        l1_head = head
        l2_head = prev
        # merge both list
        while l2_head:
            temp_1 = l1_head.next
            temp_2 = l2_head.next
            l1_head.next = l2_head
            l2_head.next = temp_1
            l1_head = temp_1
            l2_head = temp_2
        
            