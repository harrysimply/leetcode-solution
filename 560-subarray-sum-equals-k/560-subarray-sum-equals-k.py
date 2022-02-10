class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        给一个数组串和一个整数k，返回值连续子串，连续子串的和等于k。 -1000<nums[i] <=1000
        使用HashMap方法解题
        '''
        from collections import defaultdict
        count, sums = 0,0
        maps = defaultdict(int)
        maps[0] = 1
        for v in nums:
            sums += v
            if sums-k in maps:
                count += maps.get(sums-k,0)
            maps[sums] = maps.get(sums,0) + 1
        return count
        