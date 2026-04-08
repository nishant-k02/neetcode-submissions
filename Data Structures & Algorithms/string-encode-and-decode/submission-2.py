class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string = encoded_string + str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            word_extracted = s[j + 1 : j + 1 + length]
            res.append(word_extracted)
            i = j + 1 + length
        return res
