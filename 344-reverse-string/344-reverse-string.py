class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        使用O(1)空间复杂度，使用双指针算法
        
        """
        def reverse(s, i, j):
            while(i<j):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i+=1
                j-=1
        reverse(s, 0 , len(s)-1)