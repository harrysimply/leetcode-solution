class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        题目含义非常简单，m*n矩阵，其中1代表岛屿，0代表水域，找出最大的岛屿面积
        使用dfs
        有一个问题是，如何遍历所有的岛屿呢？
        '''
        r = len(grid)
        c = len(grid[0])
        def dfs(i,j):
            # 搜索条件：不越界，不为0
            if i>= 0 and i < r and j >= 0 and j < c and grid[i][j] != 0:
                grid[i][j] = 0 
                return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i, j+1) + dfs(i, j-1)
            else:
                return 0
        Areas = [dfs(i,j) for i in range(r) for j in range(c) if grid[i][j] ]
        
        return max(Areas) if Areas else 0
        