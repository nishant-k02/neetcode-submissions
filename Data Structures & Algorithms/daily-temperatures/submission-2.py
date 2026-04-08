class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        results = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                dist = stack.pop()
                results[dist] = i - dist
            stack.append(i)
        return results

                    

        