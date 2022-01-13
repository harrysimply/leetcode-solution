class Solution:
    def fib(self, n: int) -> int:
        '''
        斐波那契数列，表达式长得就像是动态规划的状态方程
        f[n] = f[n-1] + f[n-2]
        直接使用dp
        '''
        if n < 2:
            return n
        f = [0 for i in range(n+1)]
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1,1):
            f[i] = f[i-1] +f[i-2]
        return f[n]