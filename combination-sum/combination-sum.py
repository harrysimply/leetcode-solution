class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        给出一些candidates，里面是一组数字，然后看这里面的数字怎么组合可以成为target，数字也可以复用。
        target小于500，并且列表的长度为30，且数字的大小不超过200
        计算target有几种组合方式，然后如果这些组合方式里面每一个数字都是candidate里面的值，那么就列出来这些解的方式。
        首先对candidates [a, b , c, d, e, ... n]排一个序，从最小到最大,数量为n
        然后计算一个多元表达式，类似于ax1+bx2+cx3+...nxn = target,求有多少组解
        
        继续缩小范围，如果candidates里面的最小的值大于target,直接返回空解。
        如果candidate中有大于target的数，则那个数的x直接等于0
        
        将candidate从大到小排列，遍历第一个数的时候，target//n为出现的可能性
        
        参考：https://leetcode.com/problems/combination-sum/discuss/16554/Share-My-Python-Solution-beating-98.17
        
        可以在纸上画出来target减去每个item的值，当差值大于0然后进入下一轮搜索，当差值等于0则搜索结束，当差值小于0则退出搜索。
        解题思路：
        1. 先对candidate按大小个排序
        2. 使用深度优先搜索进行搜索。
        
        '''
        res = []
        
        def dfs(tempList, candidates, target):
            
            for idx,item in enumerate(candidates):
                d = target - item
                if d == 0:
                    res.append(tempList+[item])
                    break
                elif d > 0:
                    dfs(tempList+[item], candidates[idx:],d)
                else:
                    break
        dfs([], sorted(candidates), target)
        return res
                    
        
        
        