# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # approach

        # create an empty node
        # new_list = ListNode(None)
        # curr = new_list
        # while list1 and list1
        #     if list1.val<=list1.val 
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = lt2
        #         list2 = list2.next
        #     curr = curr.next

        # while list1
        #     curr.next = list1
        #     list1 = list1.next

        # while list2
        #     curr.next = list2
        #     list2 = list2.next

        
        # return new_list.next


        dummy = ListNode(None)
        curr = dummy

        while list1 and list2:
            if list1.val<=list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return dummy.next




















