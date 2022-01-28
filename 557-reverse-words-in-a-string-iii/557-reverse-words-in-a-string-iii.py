class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        翻转一句话中的每一个单词，同时句子还保持原来的顺序
        
        '''
        # def reverse(word, i,j):
        #     while(i<j):
        #         tmp = word[i]
        #         word[i] = word[j]
        #         word[j] = tmp
        #         i+=1
        #         j-=1
        res = []        
        for word in s.split(" "):
            res.append(word[::-1])
        return " ".join(res)
        