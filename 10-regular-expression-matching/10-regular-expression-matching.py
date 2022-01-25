class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        正则匹配.*的实现，
        如果pattern中不能表示setence，则返回false。
        如果pattern中包含*，则可以匹配0个或多个*前面的字符
        如果pattern中包含.，则可以匹配任意字符。
        使用回溯算法， 用条件判断代替循环
        https://www.bilibili.com/video/BV1Tb4y1R7Fs?from=search&seid=12031801529198137232&spm_id_from=333.337.0.0
        考虑两种情况，一种是完全匹配的情况，一种是pattern中出现a*,.*这种情况。
        '''
        def isMatch(s, sidx, p, pidx):
            # 回溯终止条件， pidx指针指向pattern的末尾，sidx也指向string的末尾，表示已匹配上
            if (pidx >= len(p)):
                return sidx == len(s)
            # 第一种模式：a*或.*的形式
            if (pidx + 1) < len(p) and p[pidx + 1] == '*':
                # 为了patern尽可能多的匹配string,如果pidx+2不匹配的时候则给sidx+1。
                if (isMatch(s, sidx, p, pidx+2)):
                    return True
                if (sidx < len(s)) and (p[pidx] == '.' or s[sidx]==p[pidx]):
                    return isMatch(s, sidx+1, p, pidx)
            # 第二种模式：字符完全匹配
            elif (sidx < len(s)) and (p[pidx]=='.'or s[sidx] == p[pidx]):
                    return isMatch(s, sidx+1, p, pidx+1)
        return isMatch(s,0,p,0)
            
                