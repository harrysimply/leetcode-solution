class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        在递增数组中找出来重复的数字，让重复的元素不超过2次，并且不使用额外的数组
        最后只需要返回列表长度。
        
        使用双指针可以实现O(1)空间复杂度
        
        双指针+滑动窗口
        '''
        i = 0 
        
        for j in nums:
            
            if i < 2 or j > nums[i-2]:
                nums[i] = j
                i+=1
        return i
        
        
        