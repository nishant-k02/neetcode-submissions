class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] # pairs: [temp : index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackTempIndex = stack.pop()
                result[stackTempIndex] = index - stackTempIndex
            stack.append((temp, index))
        
        return result
