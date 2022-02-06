class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        有一个m*n的0-1矩阵，计算每个矩阵距离0的距离
        给的示例是0的距离是0，1如果旁边元素是0则距离为1
        计算方向也是4个方向,找到最近的0的距离
        
        暴力解法的思路帮助理解题意：首先初始化一个同样大小的矩阵dist,然后遍历原来的矩阵，如果矩阵元素为0时，dist[i][j]为0，如果矩阵元素为1时，遍历整个mat，找到所有0元素和当前元素的距离，找到其中最小的。
        
        使用广度优先搜索，找到距离1最近的0
        '''
        height = len(mat)
        width = len(mat[0])
        q = []
        
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = "#"
        for row,column in q:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nr = row + dx
                nc = column +dy
                
                if 0 <= nr < height and 0 <= nc < width and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[row][column] + 1
                    q.append((nr, nc))
                    
        return mat