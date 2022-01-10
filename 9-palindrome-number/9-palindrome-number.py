class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        回文数字。如果一个数前后都相等则称为回文数，如果是负数则不是回文数
        # if x < 0 or str(x) !=str(x)[::-1]:
        #     return False
        # else:
        #     return True
        
        新方法： x//10 得到 前面的数字， x%10得到后面的数字，通过一个循环获得一个新的数字
        
        '''
        if x < 0:
            return False
        b = x
        res = 0
        while x > 0:
            res = 10 * res + x % 10
            
            x = x // 10
            
        return res == b
            
        
        

        