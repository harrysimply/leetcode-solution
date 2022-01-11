class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        给定一个柱子高度的列表，最高的两个柱子围成的长方形就是最大容器
        Python暴力解法容易超时：
        max_area = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                area = (j-i)* min(height[i], height[j]) 
                if area > max_area:
                    max_area = area
        return max_area
        使用双指针i,j表示最高的两个柱子的坐标，height[i]和height[j]就是两个柱子的真实坐标，找到两个相对较高的
        '''
        L, R = 0, len(height)-1
        max_area = 0
        while L < R:
            max_area =max( (R - L) * min(height[L], height[R]), max_area)
            if height[L] > height[R]:
                R-=1
            else:
                L+=1
        return max_area
            
            

        