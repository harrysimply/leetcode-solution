class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        最长公共前缀
        先挑出来第一个字符串并且设置一个index，index从0开始。从第一个字符串的第一个字符c开始遍历， 比较剩下字符串中第index位的字符和c是否相同。如果不同，则返回res。如果相同，则index加一，res拼接c。
        如果第一个字符已经遍历完了，但是其他的字符串还没有遍历完，则返回第一个字符串。
        如果其他字符已经遍历完了，而第一个字符还没有遍历完,则返回当前res
        """
        index=0
        res = ""
        for c in strs[0]:
            for item in strs[1:]:
                if index == len(item):
                    return res
                if item[index] != c:
                    return res
            res+=c
            index+=1    
        return strs[0]        
            
        
        
        