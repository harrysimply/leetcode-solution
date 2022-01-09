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
        
        
        参考： https://www.youtube.com/watch?v=aM4Iv7eEr2o
        """
        dummy = head = ListNode(0)
        carry = 0
        
        # 两数相加，直到链表为空
        while l1 != None or l2 != None:   
            # 当其中一个链表为空的时候赋值为0
            l1_val = 0 if l1 == None else l1.val
            l2_val = 0 if l2 == None else l2.val

            sum_res = 0    
            current_sum = l1_val + l2_val + carry
            carry = current_sum // 10
            new_kept_num = current_sum % 10
            # 将两数相加和与10取余的结果保存到新的链表中
            dummy.next = ListNode(new_kept_num)

            #如果链表不为空，则移动链表
            if l1 !=None: l1 = l1.next
            if l2 !=None: l2 = l2.next
            dummy = dummy.next
        if carry>0:
            new_node = ListNode(carry)
            dummy.next = new_node
        return head.next
        
            
            