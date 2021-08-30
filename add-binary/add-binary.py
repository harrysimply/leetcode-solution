class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        两个二进制字符串，相加后得到新的二进制字符串。
        下一步就需要考虑进位carry
        从两个字符串最右边列开始计算，如果大于2则进一位
        
        """
        i, j, summ, curry = len(a)-1, len(b)-1, "", 0
        
        while i>=0 or j>=0 or curry!=0:
            d1 = int(a[i]) if i >= 0 else 0 # 补齐二进制字符串长度较短空位
            d2 = int(b[j]) if j >= 0 else 0  
            summ += str((d1+d2+curry)%2)
            curry = (d1+d2+curry)//2
            i,j = i-1,j-1
        return summ[::-1]
        