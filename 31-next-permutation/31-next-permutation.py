class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        https://www.youtube.com/watch?v=9Xxv6J88KVs
        看了题目开始看不懂这个题到底想让我们干什么。。。后来看了视频才了解到是一组数字，找出来这组数组的排列组合中，比当前数字的大的数字组合中最小的那一个。如果整个数组都是逆序排列的，则返回最小升序排列数组。
        题解参考：https://www.youtube.com/watch?v=IbcQOdtmvpA
        """
        def reverse(nums, i , j):
            while i<j:
                swap(nums, i, j)
                i+=1
                j-=1
                
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
        if len(nums) == 0: return
        i = len(nums) - 2
        # 第一个循环判断特殊情况 数组从右往左一路递增
        while (i>=0 and nums[i]>=nums[i+1]):
            i-=1
        # 当出现从右往左第一个下降时，则意味着出现第一个可以交换的值
        if (i>=0):
            j = len(nums) - 1
            # 找右侧第一个比该i大的数然后交换
            while (j>0 and nums[i]>=nums[j]):
                j-=1
            swap(nums, i, j)
            # 交换完成后i右侧的数字逆序
        reverse(nums, i+1, len(nums)-1)
        
