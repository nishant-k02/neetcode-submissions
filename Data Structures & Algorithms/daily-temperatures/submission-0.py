class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        flag = False
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    results.append(j - i)
                    flag = True
                    break
            if not flag:
                results.append(0)
            flag = False
        return results

        