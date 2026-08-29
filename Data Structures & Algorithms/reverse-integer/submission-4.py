class Solution:
    def reverse(self, x: int) -> int:
        negative = 1
        if x < 0:
            negative = -1
            x *= -1
        reversedNum = 0

        while x > 0:
            reversedNum = (reversedNum * 10) + (x % 10)
            x = x // 10
        reversedNum *= negative
    
        if -(2 ** 31) <= reversedNum <= (2 ** 31):
            return reversedNum
            
        return 0