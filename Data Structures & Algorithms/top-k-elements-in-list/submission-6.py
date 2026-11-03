from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencyCounter = Counter(nums)
        resultArray = []

        sortedList = sorted(frequencyCounter.items(), key=lambda x: x[1], reverse=True)

        for key, value in sortedList[ : k]:
            resultArray.append(key)

        return resultArray
