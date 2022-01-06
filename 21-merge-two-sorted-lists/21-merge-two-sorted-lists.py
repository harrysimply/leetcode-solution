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
        
        """
        # dummy和head都是链表中的指针，区别是head指示的是链表起始的指针，dummy保存最终有序链表的指针
        dummy = head = ListNode(0) # 这里的0并无特殊含义，只是初始化一个链表，假设链表的第一个值是0，那么链表的next就是我们最终的链表
        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                # 两个链表的值比较，较小的那个就是新链表的指向
                dummy.next = list1
                # list1链表向后移动一位
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            # 新链表向后移动以为
            dummy = dummy.next
        # 比较完一轮后会有其中一个链表有多余部分，那么新链表只需要指向另一个链表剩下的部分。
        if list1 == None:
            dummy.next = list2
        else:
            dummy.next = list1
            
        return head.next