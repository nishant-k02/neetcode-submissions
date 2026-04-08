class Solution:
    def countBits(self, n: int) -> List[int]:
        final = []
        for i in range(n + 1):
            # print(i)
            count = 0
            for j in range(32):
                if i & (1 << j):
                    count += 1
            final.append(count)
            count = 0
        return final
        