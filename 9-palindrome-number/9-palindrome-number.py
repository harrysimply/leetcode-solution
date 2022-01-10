class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        回文数字。如果一个数前后都相等则称为回文数，如果是负数则不是回文数
        # if x < 0 or str(x) !=str(x)[::-1]:
        #     return False
        # else:
        #     return True
        
        新方法： x//10 得到 前面的数字， x%10得到后面的数字，res = 10 * res + x % 10 一轮循环后可以创建一个新数字
        
        '''
        if x < 0 or (x >0 and x%10==0):
            return False
        b = x
        res = 0
        while x > res:
            res = 10 * res + x % 10
            
            x = x // 10
            
        return res == x or res//10 == x
            
        
        

        