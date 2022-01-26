class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        理解下题意，在一个有序列表中找到target的位置，如果没找到就返回target在列表中的位置。必须使用O(logn)的时间复杂度。
        for idx,i in enumerate(nums):
            if i >= target:
                return idx
        return len(nums)  
        题目如果要求O(logn)则题解应该使用二分法。
        '''
        l, r = 0, len(nums)-1
        if nums[-1] < target:
            return r+1
        
        while(l<r):
            mid = l + (r-l)//2
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        return l
          