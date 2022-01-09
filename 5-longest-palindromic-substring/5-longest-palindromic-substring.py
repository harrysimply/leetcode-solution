class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        暴力解法：第一个循环从第一个字符开始遍历，下一个循环从后面的字符开始遍历，然后判断中间的字符子串是不是回文串然后找出来最长的；
        双指针法： 从字符串的第一个字符出发，用一个循环和两个指针判断左右两侧是不是回文字符，然后更新最长回文子串，分奇偶字符

        """
        res = ""
        max_len = 0
        for i in range(len(s)):
            #奇数
            l = r = i
            while l >=0  and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    res = s[l:r+1]
                    max_len = r - l +1
                l-=1
                r+=1
                
            # 偶数
            
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l+1 > max_len:
                    res = s[l:r+1]
                    max_len = r -l +1
                l-=1
                r+=1
        return res
                