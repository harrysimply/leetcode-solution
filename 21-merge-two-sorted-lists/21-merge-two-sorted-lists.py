# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy和head都是链表中的指针，区别是head指示的是链表起始的指针，dummy保存最终有序链表的指针
        dummy = head = ListNode(0)
        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1 == None:
            dummy.next = list2
        else:
            dummy.next = list1
            
        return head.next