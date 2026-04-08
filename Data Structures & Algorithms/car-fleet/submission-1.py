class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_desc = zip(position, speed)
        combined = sorted(sorted_desc, key = lambda x: x[0], reverse = True)
        # print(combined)
        time = []
        for i in range(len(combined)):
            time.append((target - combined[i][0]) / combined[i][1])
        # print(time)
        stack = [time[0]]
        # print(stack)
        for i in range(1, len(time)):
            if time[i] <= stack[-1]:
                continue
            else:
                stack.append(time[i])
        # print(stack)
        return len(stack)



