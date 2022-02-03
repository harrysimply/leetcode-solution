class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        检查s2中是否出现s1中的某种排列，而且排列中的元素只能出现一次
        
        使用HashTable和SlidingWindow，建立26字母的hashTable保存窗口命中元素数量，若命中数量与s1中的HashTable中字母命中数量相同，则返回True，负责返回False
        '''
        # 使用数字代替字母，0到25代表a到z
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]


    
        #构建一个长度为26的hash表target表示s1中每个字母出现的次数
        target = [0] * 26
        for x in A:
            target[x] +=1
        #用一个长度为26的hashmap表window表示窗口中s1中每个字母出现的次数    
        window = [0] * 26

        for i, x in enumerate(B):
            window[x] += 1
            # 当窗口长度超过s1时，i-len(A)那一位字母的计数-1
            if i >= len(A):
                window[B[i-len(A)]] -= 1
            # 如果两边的hashtable的大小一致，证明窗口内字母数量和s1中字母排列一致    
            if window == target:
                return True

        return False
            
        