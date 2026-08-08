class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        asciHash = [0] * 26

        for char in s:
            asciHash[ord(char) - ord('a')] += 1
        for char in t:
            if asciHash[ord(char) - ord('a')] == 0:
                return False
            asciHash[ord(char) - ord('a')] -= 1
        return True
        
        
        