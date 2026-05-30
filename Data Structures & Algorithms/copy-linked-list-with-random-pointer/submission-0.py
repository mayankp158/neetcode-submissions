"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # approach

        # clone all nodes from the current list to new list
        # keep storing nodes random pointer in a hashmap
        # use the hashmap to assign random pointers in new list

        if not head:
            return None
        
        new_head = Node(head.val)
        old_temp = head.next
        new_temp = new_head

        hashmap = {}
        hashmap[head] = new_head

        while old_temp:
            copy_node = Node(old_temp.val)
            new_temp.next = copy_node
            hashmap[old_temp] = copy_node
            old_temp = old_temp.next
            new_temp = new_temp.next

        old_temp = head
        new_temp = new_head

        while old_temp:
            if old_temp.random:
                new_temp.random = hashmap[old_temp.random]
            else:
                new_temp.random = None
            old_temp = old_temp.next
            new_temp = new_temp.next

        return new_head
        