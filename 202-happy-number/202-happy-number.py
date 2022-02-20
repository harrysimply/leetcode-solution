class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        不断的去拆解这个n，并计算分解数字的平方和，最后如果可以得到平方和为1，则证明这个数是一个Happy Number
        '''
        slow = n
        fast = self.digitSquareSum(n)
        while slow != fast:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(self.digitSquareSum(fast))
        return slow == 1
    
    def digitSquareSum(self, n):
        sum = 0
        while n>0:
            tmp = n% 10
            sum += tmp *tmp
            n//=10
        return sum
        
        