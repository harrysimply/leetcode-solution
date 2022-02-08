class Solution:
    def addDigits(self, num: int) -> int:
        '''
        加数字，把num拆开后再加起来，不断把所有的位数去加，知道结果变成1位，返回那一位。
        
        0 <= num <= 2^31 -1
        不使用循环或者递归方法以O(1)
        
        不使用while和for 
        '''
        if num == 0: return 0
        return 9 if num%9==0 else num%9 
        