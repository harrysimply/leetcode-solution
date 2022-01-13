class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        经典动态规划问题，n个台阶，但是只能爬1格或者2格楼梯，问有多少种可能
        当n等于1时，只有1种可能，即爬1格。
        当n等于2时，只有2种可能，即爬2格，或者爬两个1格
        ...
        
        当n等于i时，爬了i-1步时爬1格，爬了i-2步时爬2格，所以dp[i] = dp[i-1] + dp[i-2]
        
        '''
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1,1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        