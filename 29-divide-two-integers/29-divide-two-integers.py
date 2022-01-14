class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        计算两个整数的除数，不能使用任何的乘除算子。
        但是可以使用减法
        暴力解会超时：
        
        d = abs(dividend)
        dv = abs(divisor)
        res = 0
        
        while d >= dv:
            d = d-dv
            res +=1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
            
        return res
        '''
        d = abs(dividend)
        dv = abs(divisor)
        res = 0
        
        while d >= dv:
            tmp = dv
            mul = 1
            while d >= tmp:
                d -= tmp
                res += mul
                mul += mul
                tmp += tmp
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
            
        return min(2147483647, max(-2147483648, res))
