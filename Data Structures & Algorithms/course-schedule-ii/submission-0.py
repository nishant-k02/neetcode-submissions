from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseOrder = []        # Result Array

        # Creating adjacency List
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        # print(adjList)

        # Creating indegree list
        indegree = [0] * numCourses
        for i in range(numCourses):
            for element in adjList[i]:
                indegree[element] += 1
        
        # Creating queue
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            currentCourse = queue.popleft()
            courseOrder.append(currentCourse)

            for element in adjList[currentCourse]:
                indegree[element] -= 1
                if indegree[element] == 0:
                    queue.append(element)

        if len(courseOrder) == numCourses:
            return courseOrder
        return []


        