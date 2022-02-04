class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        给一个0和1组成的数组，返回最有可能的连续子数组，其中子数组拥有相同数量的0和1
        读题后觉得这个题目和双指针以及HashTable很接近
        
        用一个map去存count的和和当前index，当遇到0时，count-1，当遇到1时，count+1
        并把当前count和index保存在map中
        当count值再次出现时，两个index之差就是最长长度，maxLength = max(maxLenth, index-hashTable(count))
        
        '''
        hashTable = {0:-1}
        count = 0
        maxLength = 0
        for index,i in enumerate(nums):
            if i == 0:
                count -=1
            else:
                count +=1
            if count in hashTable:
                maxLength = max(maxLength, index-hashTable[count])
            else:
                hashTable[count] = index
        return maxLength