class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        大数以列表形式展示，从最高位向最低位，最后一位在最左边。给最左边加一。
        然后返回最终列表。
        如果最后一位加1小于9，给最后一位加1然后返回整体列表
        如果最后一位加1等于9，给前一位加1,再判断
        '''
        n = len(digits)
        for i in range(n-1,-1,-1):
            # 如果最后一位或当前位小于9直接+1返回，终止
            if digits[i] < 9:
                digits[i] +=1
                return digits
            # 如果最后一位等于9，则该位赋0，进入下一轮循环
            digits[i] = 0
        
        # 如果便利完一遍还没有得到结果，证明这个数组全是9
        new_digits = [0 for i in range(n+1)]
        new_digits[0] = 1
        return new_digits
        