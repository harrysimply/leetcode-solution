class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count = 0
        # for item in nums:
        #     if item == val:
        #         count +=1
        #         nums.remove(item)
        '''
        参考官方solution, 双指针方法:当nums[i]等于val时跳过，当不等时，将nums[i]拷贝nums[j]，同时移动i和j,直到i走完一遍循环。
        '''
        j=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j
        
        