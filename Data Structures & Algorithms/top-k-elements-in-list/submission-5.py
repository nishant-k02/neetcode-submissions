class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqCounter = {}
        resultArray = []

        for element in nums:
            if element in freqCounter:
                freqCounter[element] += 1
            else:
                freqCounter[element] = 1
        
        sortedList = sorted(freqCounter.items(), key=lambda x: x[1], reverse=True)

        for key, value in sortedList[ : k]:
            resultArray.append(key)
            
        return resultArray
