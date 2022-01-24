class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        这道题使用栈来保存最长有效括号长度。当遇到左括号，将左括号压入栈，当遇到右边括号，左边括号出栈，并将最长括号长度+1。
        
        '''
        stack = []
        stack.append(-1)
        res = 0
        for idx,i in enumerate(s):
            if i == '(':
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    res = max(res, idx - stack[-1])
        return res
        