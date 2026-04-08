class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        n = len(s)

        for i in range(1, n):
            if stack and (
                (s[i] == ')' and stack[-1] == '(') or 
                (s[i] == ']' and stack[-1] == '[') or 
                (s[i] == '}' and stack[-1] == '{')
            ):
                stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False

            
        