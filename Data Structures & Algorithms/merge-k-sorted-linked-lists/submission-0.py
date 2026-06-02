# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # approach -> Brute force TC = nk (n = no. of nodes, k = no. of link lists)
        # if lists is empty:
        #     return
        # n = len(lists)
        # if n==1:
        #     return lists[0]
        # else:
            # l1 = lists[0]
            # for i in range(1, n):
            #     l1 = self.merge(l1,lists[i]) # similar to merge sorted list code

            # return l1.head()

        # optimised approach

        # if len(lists)==0 or not lists:
        #     return []
        # select set of 2 different lists in each iteration -> merge function
        # set given lists = merged_lists -> call again merge funtion

        # merged_lists = []
        # while len(lists)>1:
        #     for i in range(0, len(lists), 2)
        #         l1 = lists[i]
        #         if i+1 < len(lists):
        #             l2 = lists[i+1]
        #         else:
        #             l2 = None
        #         merged_lists.append(merge_lists(l1,l2))
        #     lists = merged_lists
        
        # merge_lists(l1,l2):
        #     dummy = ListNode()
        #     head = dummy

        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             head.next = l1
        #             l1 = l1.next
        #         else:
        #             head.next = l2
        #             l2 = l2.next
        #         head = head.next
            
        #     if l1:
        #         head.next = l1

        #     if l2:
        #         head.next = l2

        #     return dummy.next

        if len(lists)==0 or not lists:
            return None

        while len(lists)>1:
            merged_lists = []
            n = len(lists)
            for i in range(0,n,2):
                l1 = lists[i]
                if (i+1) < n:
                    l2 = lists[i+1]
                else:
                    l2 = None

                merged_lists.append(self.merge_lists(l1,l2))
            lists =  merged_lists
        return lists[0]

    def merge_lists(self, l1, l2):
        dummy = ListNode(None)
        head = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            
            head = head.next

        if l1:
            head.next = l1

        if l2:
            head.next = l2

        return dummy.next