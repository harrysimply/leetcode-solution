class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        将列表的每一位向右移动k位，然后返回新的列表，如果到最后一位则将最后一位移动到第一位
        使用O(1)的空间复杂度，考虑使用双指针
        问题变成[1,2,3,4,5,6,7],先将[1，2，3，4]reverse变成[4,3,2,1],然后将[5,6,7]变成[7,6,5],最后将[4,3,2,1,7,6,5]整体reverse，变成[5,6,7,1,2,3,4]
        """
        # 使用双指针实现数组逆序
        def reverse(nums,i,j):
            tmp =0
            while(i<j):
                tmp = nums[i] 
                nums[i] = nums[j]
                nums[j] = tmp
                i+=1
                j-=1
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1-k)
        reverse(nums, len(nums)-k, len(nums)-1)
        reverse(nums, 0, len(nums)-1)