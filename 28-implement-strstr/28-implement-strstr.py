class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        '''
        a needle in a haystack means something that is impossible or extremely difficult to find, especially because the area you have to search is too large. 在中文里意味着大海捞针。
        
        如果在稻草堆里找到针，则返回针在稻草堆里的位置，如果不存在返回-1。如果针是空值则返回0.
        
        一行代码AC: return haystack.find(needle) 
        如果不使用python内建函数：
        
        '''
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1