class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        temp = x
        x = abs(x)
        while x > 0:
            ans += str(x % 10)
            x = x // 10
        if temp > 0 and int(ans) <= (2 ** 31) - 1:
            return int(ans)
        elif temp < 0 and -(int(ans)) >= -(2 ** 31):
            return -(int(ans))
        else:
            return 0