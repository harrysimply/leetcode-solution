class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        一种O(n)复杂度的思路，如果想知道2和谁相加等于9，先存储2的下标和（9-2）的值，当nums[i]等于（9-2）时，返回2的下标和当前i的值
        参考：https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time
        用一个字典存储需求的值和当前下标，遍历一遍，当需求的值出现时返回之前的下标与当前需求值的下标。
        """
        buffer_dic = {}

        for i in range(nums.__len__()):
            if nums[i] not in buffer_dic:
                buffer_dic[target-nums[i]] = i
            else:
                return [buffer_dic[nums[i]],i]
        
        