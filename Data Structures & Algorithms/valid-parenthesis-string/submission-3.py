class Solution:
    def checkValidString(self, s: str) -> bool:
        min_range = 0
        max_range = 0
        for char in s:
            if char == '(':
                min_range += 1
                max_range += 1
            elif char == ')':
                min_range -= 1
                max_range -= 1
            else:   # if its '*'
                min_range -= 1
                max_range += 1
            if max_range < 0:
                return False
            if min_range < 0:
                min_range = 0
        return min_range == 0
        