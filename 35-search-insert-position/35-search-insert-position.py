class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        理解下题意，在一个有序列表中找到target的位置，如果没找到就返回target在列表中的位置。必须使用O(logn)的时间复杂度。
        '''
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            else:
                for idx,i in enumerate(nums[1:]):
                    if i> target:
                        return idx+1