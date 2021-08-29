class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        暴力思路：每个数字和后面的数字加起来的和如果等于target，便返回下标。
        """
        for idx, i in enumerate(nums[0:len(nums)-1]):
            for idx2,j in enumerate(nums[idx+1:len(nums)]):
                if i+j == target:
                    return [idx,idx+idx2+1]