class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversedNum = 0

        while x:
            reversedNum = (reversedNum * 10) + (x % 10)
            x = x // 10
            
        reversedNum *= sign
    
        if -(2 ** 31) <= reversedNum <= (2 ** 31):
            return reversedNum

        return 0