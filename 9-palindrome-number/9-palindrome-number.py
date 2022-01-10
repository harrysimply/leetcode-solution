class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        回文数字。如果一个数前后都相等则称为回文数，如果是负数则不是回文数
        '''
        if x < 0 or str(x) !=str(x)[::-1]:
            return False
        else:
            return True
        