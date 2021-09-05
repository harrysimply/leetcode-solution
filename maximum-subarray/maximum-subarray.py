class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        比较一个列表中所有连续子串的最大和，并返回最大的数字。
        
        开局一个循环，从列表的第一个值开始循环，然后计算从现在到末尾的和的最大值，时间复杂度为O(n2)
        
        使用动态规划，将问题定义为每个以i下标结尾的item的子序列中最大值是多少，通过以dp[0]的最大值和以dp[1]最大值，以及dp[n-1]时候的最大值，求出dp[n]时候的最大值。dp[0] = nums[0], dp[1] = max(nums[1]+ dp[0],nums[1])
        dp[i-1] 和 array[i]分情况：
        dp[i-1]>0 array[i]>0, 则dp[i] = dp[i-1]+array[i]
        dp[i-1]>0 array[i]<0, 则dp[i] = dp[i-1]+array[i]
        dp[i-1]<0 array[i]>0, 则dp[i] = array[i]
        dp[i-1]<0 array[i]<0, 则dp[i] = array[i]
        得出
        dp[i] = max(dp[i-1]+array[i], array[i])
        最终解为max(dp)
        时间复杂度为O(n)
        
        如果将i中最后一位的dp值和最大值做比较，则可以出现kadane算法
        用一个指针保存迄今为止的最大值，用一个指针保存当前下标为i的子序列的最大值，最终返回两者的最大值。
        时间复杂度O(n),空间复杂度O(1)
        """
        dp = [ 0 for _ in nums ]
        last_max = max_num = nums[0]
        
        for i in range(1,len(nums)):
            last_max = max(last_max+nums[i],nums[i])
            max_num = max(last_max, max_num)
            
        return max_num
        
            
        
        