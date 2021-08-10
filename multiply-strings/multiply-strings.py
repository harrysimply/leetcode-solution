class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        第一眼看题，求两字符串组成的数的乘积，但是不能用内置函数转换，也不能转换输入
        如果想做乘法，就必须某种方式将字符转换成为数字。
        因此，使用map映射，将字符串转换为数字，然后进行10进制乘法
        
        """

        def convert_string_to_num(num_string):
            char_num_map = {
                "0":0,
                "1":1,
                "2":2,
                "3":3,
                "4":4,
                "5":5, "6":6,"7":7,"8":8,"9":9,
            }
            char_length = len(num_string)
            num_list = [char_num_map[i] for i in num_string]
            num_list.reverse()
            int_num = 0
            for idx, j in enumerate(num_list):
                int_num+=j*(10**idx)
            return int_num
            
        res = convert_string_to_num(num1)* convert_string_to_num(num2)
        return str(res)