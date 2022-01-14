class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        给一个整数，计算他的开方数是多少
        x = res * res 计算res
        从0开始遍历res，如果res^2 > x 返回res
        '''
        res = 0
        
        while res*res <= x:
            
            if res*res == x:
                return res
            res +=1
            
        return res-1