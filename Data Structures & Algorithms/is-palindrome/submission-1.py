class Solution:
    def isPalindrome(self, s: str) -> bool:
        inputs = []
        final = []
        for i in s:
            if i.isalnum():
                inputs.append(i.lower())
        # print(inputs)
        for i in inputs[::-1]:
            final.append(i)
        
        if final == inputs:
            return True
        else:
            return False
        