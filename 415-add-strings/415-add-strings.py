class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        两个字符串相加，不能使用内建库把字符串直接转成数字
        但是可以把单个数字字符转成数字
        先将字符串逆序，然后累加
    
        """
        carry =0
        res = ""
        count = max(len(num1),len(num2))
        index = 0
        while index < count: 
            current_sum = 0
            
            n1 = int(num1[::-1][index]) if index < len(num1) else 0
            n2 = int(num2[::-1][index]) if index < len(num2) else 0
            
            current_sum = n1 + n2 + carry
                
            carry = current_sum // 10
                
            kept_sum = current_sum % 10 
            res += str(kept_sum)
            index +=1
        if carry > 0:
            res += str(carry)
        return res[::-1]
        
        