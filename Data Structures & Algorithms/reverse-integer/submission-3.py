class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        ans = ''
        sign = -1 if x < 0 else 1
        temp = x
        x = abs(x)
        while x:
            ans += str(x % 10)
            x = x // 10
        if (-2**31 <= int(ans) <= 2**31 - 1):
            return int(ans) * sign
        else:
            return 0