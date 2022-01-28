class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        翻转一句话中的每一个单词，同时句子还保持原来的顺序
        
        '''

        
        return " ".join(s.split(" ")[::-1])[::-1]
        