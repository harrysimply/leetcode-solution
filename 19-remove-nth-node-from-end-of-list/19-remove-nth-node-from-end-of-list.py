# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        找到倒数第n个链表节点，然后删掉它。
        参考官方题解可以使用快慢指针法。
        '''
        fast, slow =  head, head
        
        # 先让快指针移动n步
        for _ in range(n):
            fast = fast.next
        # 如果快指针移动n步就到链表的结尾了，表示删除的就是第一位
        if not fast:
            return head.next
        
        # 当fast还没到结尾时循环不要\U0001f442
        while fast.next:
            fast = fast.next
            slow = slow.next
         
        slow.next = slow.next.next
        return head
            
        