# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        反转单链表，返回反转链表
        prev = None
        cur = head
        
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n 
        return prev
        
        '''
        return self._reverse(head)
        
    def _reverse(self,node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        