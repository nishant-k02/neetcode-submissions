class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        for i in range(len(temperatures)):
            days = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    days = j - i
                    break
        
            results.append(days)
            
        return results

        