from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # creating Adjancency List
        adjList = [[] for _ in range(n)]
        for source, destination, price in flights:
            adjList[source].append((destination, price))
        # print(adjList)

        # creating distance Array
        distArray = [float('inf')] * n
        distArray[src] = 0              # setting source price as 0

        queue = deque()
        queue.append((0, src, 0))         # stores stops, source, price

        while queue:
            currentStops, currentSource, currentPrice = queue.popleft()

            if currentStops > k:
                continue
            
            for nsource, nprice in adjList[currentSource]:
                if currentStops <= k and distArray[nsource] > currentPrice + nprice:
                    newPrice = currentPrice + nprice
                    distArray[nsource] = newPrice
                    queue.append((currentStops + 1, nsource, newPrice))

        if distArray[dst] == float('inf'):
            return -1

        return distArray[dst]

        