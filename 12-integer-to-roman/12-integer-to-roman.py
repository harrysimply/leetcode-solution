class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        整数转换为罗马数字的问题
        
        参考：https://www.youtube.com/watch?v=ohBNdSJyLh8
        特殊规则：
        I出现在V的左边就是4，出现在X的左边就是9
        X出现在L的左边就是40，出现在C的左边就是90
        C出现在D的左边就是400，出现在M的左边就是900
        
        最大数是3999
        '''
        
        symList = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],
                  ['C',100],['CD',400],['D',500],['CM',900],['M',1000]]
        res =""
        for sym, val in reversed(symList):
            if num // val :
                res +=num // val * sym
                num = num % val
        return res        
        
        