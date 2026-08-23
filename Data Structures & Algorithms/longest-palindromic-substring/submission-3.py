class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultIndex, resultLen = 0, 0
        n = len(s)
    
        for i in range(n):

            # odd length
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > resultLen:
                    resultIndex = left
                    resultLen = right - left + 1
                left -= 1
                right += 1

            # even length
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > resultLen:
                    resultIndex = left
                    resultLen = right - left + 1
                left -= 1
                right += 1

        return s[resultIndex : resultIndex + resultLen]
                 

        