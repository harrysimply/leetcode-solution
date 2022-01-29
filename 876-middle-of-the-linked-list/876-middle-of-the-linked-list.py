# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        链表问题，找到中间的那个节点
        如果链表中间有两个节点，则返回第二个节点头
        
        链表并没有知道长度的接口，使用快慢双指针解决问题。
        快指针是慢指针速度的两倍，当快指针到达列表的尾部，慢指针必定到达列表的中间
        '''
        
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        