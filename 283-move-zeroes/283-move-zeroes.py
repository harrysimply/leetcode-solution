class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        使用双指针
        使用两个指针来记录0值和非0值，explorer指针用来探索非0位，anchor指针表示结果数组，如果有非0位，则互换explorer和anchor位的值。
        """
        anchor = 0
        
        for explorer in range(len(nums)):
            if nums[explorer] !=0 :
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor +=1