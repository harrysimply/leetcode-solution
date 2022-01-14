class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        给一个整数，计算他的开方数是多少
        x = res * res 计算res
        从0开始遍历res，如果res^2 > x 返回res
                res = 0
        
        while res*res <= x:
            
            if res*res == x:
                return res
            res +=1
            
        return res-1
        空间O(1),时间O(n)
        也可以使用二分查找，空间复杂度O(1)时间复杂度降低到O(logn)
        '''
        l,r = 1, x
        if x < 2:
            return x
        while(l < r):
            mid = l + (r-l) // 2
            if mid * mid  == x:
                return mid
            elif mid * mid > x:
                r = mid
            elif mid * mid < x:
                l = mid + 1 # 跳出循环的关键
        return l-1
        
        
