class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        第一眼看题，求两字符串组成的数的乘积，但是不能用内置函数转换，也不能转换输入
        如果想做乘法，就必须某种方式将字符转换成为数字。
        因此，使用map映射，将字符串转换为数字，然后进行10进制乘法
        
        """

        def to_int(num_string):
            num_map = {str(i):i for i in range(10)}
            int_num = 0
            for j in num_string:
                int_num=int_num*10+num_map[j]
            return int_num
            
        res = to_int(num1)* to_int(num2)
        return str(res)