class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        官方例题集中的滑动窗口例题
        
        找到题目中的最长不包含重复字符串的子串
        使用一个hashset
        '''
        l= 0
        res = 0
        lss = set()
        # 扩大窗口
        for r in range(len(s)):
            # 缩小窗口的条件
            while s[r] in lss:
                lss.remove(s[l])
                l += 1
            lss.add(s[r])
            res = max(res, r-l+1)   
                
        return res
                
            