class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        移除有顺序列表中重复的数字，最终返回移除重复数字后的列表长度。
        要求空间复杂度（1）
        从列表的第一个数开始，后面的数字如果重复则把后面的数字向前覆盖一位
        '''
        if len(nums) < 2 : return len(nums)
        a = 1 
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[a] = nums[i]
                a+=1
        return a
            
        