class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        这道题选择找模式的方式解答
        
        PAYPALISHIRING, 当numRows = 4
        row 0: 0 + 6 + 6
        row 1: 1 + 4 + 2 + 4 + 2
        row 2: 2 + 2 + 4 + 2
        row 3: 3 + 6 
        
        numRows = 3
        row 0: 0 + 4 + 4 + 4
        row 1: 1 + 2 + 2 + 2 + 2 + 2
        row 2: 2 + 4 + 4
        
        numRows = 2
        row 0: 0 + 2 + 2 + 2 + 2 + 2 + 2
        row 1: 1 + 2 + 2 + 2 + 2 + 2 + 2
        
        4 -> 6
        3 -> 4
        2 -> 2
        1 -> 0
        
        cycle = numRows*2 -2
        
        
        """
        if numRows == 1:
            return s
        
        cycle = numRows*2 - 2
        res = []
        for i in range(numRows):
            
            for j in range(i, len(s), cycle):
                res.append(s[j])
                k = j + cycle - 2*i
                if i !=0 and i != (numRows -1) and k < len(s):
                    res.append(s[k])
                
        return ''.join(res)