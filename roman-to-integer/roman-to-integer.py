class Solution:
    def romanToInt(self, s: str) -> int:
        """
        I -> 1
        IV -> 4
        V -> 5
        IX -> 9
        X -> 10
        XL -> 40
        L -> 50
        XC -> 90
        C -> 100
        CD -> 400
        D -> 500
        CM -> 900
        M -> 1000
        特殊情况：如果V左边有I，两个字符表示的就是4，如果X左边有I，两个字符表示的就是9。。。
        可以归结为一个求和问题，他们有一个规律是如果左边的数小于右边的数，那么数字就是右边的数减去左边的数。
        """
        _dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        prev = 0
        sum = 0
        for c in s[::-1]:
            curr = _dict[c]
            if curr < prev:
                sum -= curr
            else:
                sum += curr
                prev = curr
        return sum
                
            
            
        
        
        
        