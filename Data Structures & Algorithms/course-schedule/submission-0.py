from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating adjacency list
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        # print(adjList)

        # creating indegree list
        indegree = [0] * numCourses
        for i in range(numCourses):
            for element in adjList[i]:
                indegree[element] += 1
        # print(indegree)
        
        # creating queue
        queue = deque()
        for element in range(numCourses):
            if indegree[element] == 0:
                queue.append(element)
        # print(queue)

        count = 0

        while queue:
            currentCourse = queue.popleft()
            count += 1

            for element in adjList[currentCourse]:
                indegree[element] -= 1
                if indegree[element] == 0:
                    queue.append(element)

        if count == numCourses:
            return True

        return False


        

