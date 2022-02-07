# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        参考youtube视频讲解：https://www.youtube.com/watch?v=K63Mjf-H0B0
        python的链表中保存了一段有序节点，每个节点会保存当前节点值val和下一个节点内容next
        
        挑战：使用递归算法去做这道题
        
        """
        if not list2:
            return list1
        if not list1:
            return list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
        