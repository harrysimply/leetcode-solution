class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        记得之前看过一节算法课，如果要求时间复杂度为O(logn)则一定使用二分查找
        题意为，当遇到一个升序的数组，判断target是否在数组中，以及在数组中的位置。
        二分法从两边开始搜索，如果中间的数字比target小了，则中间的数组变成左边界。
        '''
        l, r = 0, len(nums)-1
        
        while (l<=r):
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1 
            elif target < nums[mid] :
                r = mid - 1
            else:
                return mid

        
        return -1
        