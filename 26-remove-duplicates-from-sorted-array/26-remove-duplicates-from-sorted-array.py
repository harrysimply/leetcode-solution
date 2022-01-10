class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        移除有顺序列表中重复的数字，最终返回移除重复数字后的列表长度。
        要求空间复杂度（1）
        从列表的第一个数开始，后面的数字如果重复则删掉后面的数字
        '''
        if len(nums) == 0 : return None
        a = nums[0]
        for item in nums[1:]:
            if item == a:
                nums.remove(item)
            else:
                a = item
        return len(nums)
            
        