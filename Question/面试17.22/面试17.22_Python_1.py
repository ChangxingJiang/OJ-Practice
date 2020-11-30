import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        if endWord not in wordList:
            return []

        all_words = [beginWord] + wordList

        graph = {word: set() for word in all_words}

        for i in range(len(all_words)):
            for j in range(i + 1, len(all_words)):
                word1, word2 = all_words[i], all_words[j]
                if len(word1) == len(word2):
                    differ = 0
                    for k in range(len(word1)):
                        if word1[k] != word2[k]:
                            differ += 1
                    if differ == 1:
                        graph[word1].add(word2)
                        graph[word2].add(word1)

        visited = {beginWord}
        queue = collections.deque([(beginWord, [beginWord])])
        while queue:
            word, path = queue.popleft()
            for near in graph[word]:
                if near not in visited:
                    if near == endWord:
                        return path + [near]
                    visited.add(near)
                    queue.append((near, path + [near]))

        return []


if __name__ == "__main__":
    # ["hit","hot","dot","lot","log","cog"]
    print(Solution().findLadders(beginWord="hit",
                                 endWord="cog",
                                 wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

    # []
    print(Solution().findLadders(beginWord="hit",
                                 endWord="cog",
                                 wordList=["hot", "dot", "dog", "lot", "log"]))
