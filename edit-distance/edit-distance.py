class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        这道题的写法需要理解莱文斯坦距离（Levinstein Distance）公式的含义。
        根据莱文斯坦公示完成代码。
        参考：https://www.youtube.com/watch?v=b6AGUjqIPsA
        """
        row = len(word1) + 1
        column = len(word2) + 1
        
        cache = [ [0]*column for i in range(row) ]
        
        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:
                    cache[i][j] = 0
                elif i == 0 and j != 0:
                    cache[i][j] = j
                elif j == 0 and i != 0:
                    cache[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        cache[i][j] = cache[i-1][j-1]
                    else:
                        replace = cache[i-1][j-1] + 1
                        insert = cache[i][j-1] + 1
                        remove = cache[i-1][j] + 1
                        cache[i][j] = min(replace, insert, remove)
                    
                
        return cache[row-1][column-1]  