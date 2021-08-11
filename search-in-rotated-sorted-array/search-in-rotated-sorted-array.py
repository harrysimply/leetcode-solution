class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        num是一个升序的数组。
        nums在传入函数之前，数组就已经被旋转过了。
        返回某target在nums中的index。
        看测试用例貌似跟旋不旋转关系不大，就是看某元素在列表中的索引？
        """
        if target not in nums:
            return -1
        else:
            return nums.index(target)
        