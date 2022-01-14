class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        计算x的n次指数是多少？
        当n是正整数时，得到的是正整数；当x是负指数时，得到的是小数
        使用暴力解法会超时：
        res = 1.0
        if n > 0:
            
            for i in range(n):
                res*=x
            return res 
        elif n == 0:
            return res
        else:
            new_n = abs(n)
            
            for i in range(new_n):
                res *=x
            return 1 / res
                
        使用二分法，使
        x^10 = x^5 * x^5
        x^ 5 = x * x^2 * x^ 2
        x^2 = x^1* x^1
        x^1 = x * x^0 * x^0
        使用二分法计算，时间复杂度位O(logn)
        '''
        
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            tmp = helper(x, n//2)
            return tmp*tmp if n%2 ==0 else x*tmp*tmp
        
        
        res = helper(x, abs(n))
        
        return res if n > 0 else 1/res
        
        

        