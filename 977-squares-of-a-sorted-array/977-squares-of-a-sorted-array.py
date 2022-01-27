class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        nums是一个按照顺序排列的数组，题目要求将数组的元素取二次方后重新按顺序返回
        nums = [i*i for i in nums]
        return sorted(nums)
        题目说要使用O(n)的时间复杂度，因此考虑使用双指针的方法
        '''
        l, r = 0, len(nums)-1
        res = []
        for i in range(len(nums)):
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r]*nums[r])
                r-=1
        return res[::-1]
                
                
        
        