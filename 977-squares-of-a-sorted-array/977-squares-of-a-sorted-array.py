class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        nums是一个按照顺序排列的数组，题目要求将数组的元素取二次方后重新按顺序返回
        
        '''
        nums = [i*i for i in nums]
        return sorted(nums)