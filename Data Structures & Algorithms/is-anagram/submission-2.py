class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sort1 = sorted(s)
        count1 = Counter(sort1)
        print(count1)
        sort2 = sorted(t)
        count2 = Counter(sort2)
        print(count2)
        for (k,v), (k2,v2) in zip(count1.items(), count2.items()):
            if k != k2 or v != v2:
                return False
                break
        return True
        