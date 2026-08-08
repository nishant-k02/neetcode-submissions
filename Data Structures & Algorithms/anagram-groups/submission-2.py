from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            anagramMap[key].append(string)
        return list(anagramMap.values())

        
        