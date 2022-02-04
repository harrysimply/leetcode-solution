class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        flood fill,涂色功能。每种数字就代表一种颜色。sr和sc组成坐标是涂色坐标，运行后sr和sc周围相同的色彩都应该是同样的颜色
        
        '''
        r = len(image)-1
        c = len(image[0])-1
        color = image[sr][sc]
        def dfs(i,j):
            # 搜索终止条件1: 数组越界
            if i < 0 or i > r or j < 0 or j > c:
                return
            # 搜索终止条件2: 新颜色和旧颜色相同，或者不属于同一个色块
            if color == newColor or color != image[i][j]:
                return
            image[i][j] = newColor
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
            
        dfs(sr,sc)
        return image
        
            
        