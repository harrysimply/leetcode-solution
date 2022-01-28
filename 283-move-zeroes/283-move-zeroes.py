class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        使用双指针
        使用一个指针来记录结果非0的位数
        """
        anchor = 0
        
        for explorer in range(len(nums)):
            if nums[explorer] !=0 :
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor +=1