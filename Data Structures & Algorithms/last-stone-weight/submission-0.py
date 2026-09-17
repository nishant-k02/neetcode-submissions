class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            h1 = stones.pop()       #the heaviest stone

            if not stones:
                return h1
            h2 = stones.pop()       #second heaviest stone

            if h1 > h2:
                for i in range(len(stones) + 1):
                    # print(len(stones))
                    if i == len(stones) or stones[i] >= h1 - h2:
                        stones.insert(i, h1 - h2)
                        break
        return 0