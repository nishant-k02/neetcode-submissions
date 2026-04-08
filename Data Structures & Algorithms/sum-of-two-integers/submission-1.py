class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF   #limiting number to 32 bits
        MAX_INT = 0x7FFFFFFF

        while (b != 0):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
             
            
        # Handle negative results (since Python ints don't overflow)
        return a if a <= MAX_INT else ~(a ^ mask)
        
        