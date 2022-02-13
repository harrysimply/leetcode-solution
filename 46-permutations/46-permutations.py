class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        给出一个包含不同整数的数组，返回所有可能的排列
        1=<nums.length <=6
        经典回溯题目 决策树
        '''
        def backtrack(res, path, nums):
            # 当path的长度已经到达nums长度，证明已经搜索到树底了，不加拷贝则res为空串
            if len(path) == len(nums):
                res.append(path.copy())
            else:
                for i in range(len(nums)):
                    # 如果path中出现num[i]则跳过
                    if nums[i] in path:
                        continue
                    path.append(nums[i])
                    # 向下继续遍历
                    backtrack(res, path, nums)
                    # 回溯
                    path.pop()
        res = []            
        backtrack(res, [], nums)
        return res
        