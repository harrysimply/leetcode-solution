class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        m*n矩阵，0代表空元素，1代表新鲜橘子，2代表坏掉的橘子
        每一分钟，坏掉橘子四周的新鲜橘子都会坏掉
        返回全部橙子被腐蚀完所需要的分钟数，如果不可能则返回-1
        二维矩阵，和0-1矩阵相似，可以使用bfs思路
        先将所有的坏橙子放到一个队列中，
        '''
        from collections import deque
        
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        
        fresh_cnt = 0
        
        rotten = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        minutes_passed = 0
        
        while rotten and fresh_cnt > 0:
            
            minutes_passed += 1
            
            for _ in range(len(rotten)):
                x,y = rotten.popleft()
                for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                    xx,yy = x+dx, y+dy
                    if xx < 0 or xx==rows or yy<0 or yy ==cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh_cnt-=1
                    grid[xx][yy] = 2
                    
                    rotten.append((xx,yy))
        return minutes_passed if fresh_cnt == 0 else -1
        