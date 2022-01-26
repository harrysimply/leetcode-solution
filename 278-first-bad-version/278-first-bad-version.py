# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        假如你是一个产品经理，现在有n个版本，其中某一个版本有问题导致后续版本都出现了问题。
        现在题目提供了一个查询问题版本的接口，需要找出来问题版本是哪个，尽可能少的调api。
        if n == 1 and isBadVersion(1):
            return 1
        for i in range(1,n+1):
            if isBadVersion(i):
                return i
        使用暴力解会超时。
        使用二分搜索
        '''
        l,r = 1, n
        
        while (l<r):
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l
        
