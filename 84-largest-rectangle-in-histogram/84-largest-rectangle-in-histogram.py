class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        柱状图的最大面积，和之前的围成最大面积区域问题有点像
        先遍历一遍所有柱状图的面积，找出最大面积的柱子然后把结果给res
        之后最大面积的矩形都是近邻柱子的面积
        '''
        maxArea =0
        stack = [] #pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea
        