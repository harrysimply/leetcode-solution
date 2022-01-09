# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        实际上是十进制加数运算，但是数据都逆序存放在单链表中，考虑两种情况：
        1. 两个单链表中的数字相加小于9，新的结果链表的值为两数之和
        2. 两个单链表中的数字相加大于等于10，新的结果连表值为两数之和的各位，并且链表的下一位加1.
        
        如果两个相加的链表有一个链表加完了，则新链表的next可以指向没加完的链表。
        """
        dummy = head = ListNode(0)
        carry = 0
        
        while l1 != None or l2 != None:   
            if l1 == None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 == None:
                l2_val = 0
            else:
                l2_val = l2.val
            sum_res = 0    
            current_sum = l1_val + l2_val + carry
            carry = current_sum // 10
            new_kept_num = current_sum % 10
            dummy.next = ListNode(new_kept_num)

            if l1 !=None: l1 = l1.next
            if l2 !=None: l2 = l2.next
            dummy = dummy.next
        if carry>0:
            new_node = ListNode(carry)
            dummy.next = new_node
        return head.next
        
            
            