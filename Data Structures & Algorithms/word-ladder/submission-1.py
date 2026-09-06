from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        listSet = set(wordList)
        queue =  deque([(beginWord, 1)])        # current word and length
        listSet.discard(beginWord)              # removing element which is visited

        while queue:
            currentWord, currLength = queue.popleft()

            if currentWord == endWord:
                return currLength

            for i in range(len(currentWord)):
                for char in string.ascii_lowercase:
                    newWord = ( 
                        currentWord[ : i] 
                        + char
                        + currentWord[i + 1:]
                    )
                
                    if newWord in listSet:
                        listSet.discard(newWord)
                        queue.append((newWord, currLength + 1))
                    
        return 0
            
