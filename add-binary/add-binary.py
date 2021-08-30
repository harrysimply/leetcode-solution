class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        在面试时肯定会被干掉的解法： 
        """
        
        int_a = int(a, 2)
        int_b = int(b, 2)
        return str(bin(int_a + int_b))[2:]
        