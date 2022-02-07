class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        给两个整数n和k，返回所有可能的[1,n]集合中k长度的组合
        边界条件： 1<n<=20, 1<k <=n
        def dfs(nums, k , index, path, res):
            if k == 0:
                res.append(path)

            for i in range(index, len(nums)):
                dfs(nums, k-1, i+1, path+[nums[i]], res)
        res = []
        dfs(range(1,n+1),k,0,[], res)
        return res
        '''
        res = []
        
        def backtrack(start, comb):
            if len(comb)==k:
                res.append(comb.copy())
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        return res
                

        
        