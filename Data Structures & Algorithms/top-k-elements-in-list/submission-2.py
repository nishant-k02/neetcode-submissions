from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []
        count = 0
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_freq)

        for key, values in sorted_freq.items():
            if count < k:
                ans.append(key)
                count += 1
        return ans

        