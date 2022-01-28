# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        找到倒数第n个链表节点，然后删掉它。
        参考官方节点，可以使用快慢指针法。
        '''
        fast, slow =  head, head
        
        for _ in range(n):
            # 让快指针移动n步
            fast = fast.next
        # 如果快指针已经到头，则证明要n是链表长度，因此需要删除第一个链表节点，直接返回第二个链表
        if not fast:
            return head.next
        # 当fast.next不为空时，移动快慢指针，直到fast.next为None
        while fast.next:
            slow, fast = slow.next, fast.next
        # 此时，删掉slow慢指针的后一个链表节点
        slow.next = slow.next.next
        return head
            
        