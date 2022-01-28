class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        一个递增数组和一个目标数，在递增数组中找到两个数的和是目标数，最后返回下标
        使用双指针，设置左右两个指针，左边指针数值+右边指针数值，如果大了，那么右边指针左移，如果小了，那么左边指针右移最后如果和target相等则返回指针
        '''
        l,r = 0, len(numbers)-1
        while(l< r):
            if numbers[l]+ numbers[r] == target:
                return l+1, r+1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1
        