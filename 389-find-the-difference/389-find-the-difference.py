
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        两个字符串s和t,其中t是s打乱后生成的，并且t还会再加一个字母
        返回新加的一个字符
        
        可以统计t中的每个字母出现的次数，遍历这个map，如果s出现这个词则map计数-1，最后找出来map中值为1的字母
        '''
        from collections import defaultdict
        hashSet = defaultdict(int)
        for i in t:
            hashSet[i] += 1
        for i in s:
            if i in hashSet:
                hashSet[i] -=1
        for k,v in hashSet.items():
            if v != 0:
                return k
        