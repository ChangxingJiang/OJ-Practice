import collections
from typing import List


class Solution:
    def __init__(self):
        self.endWord = ""
        self.graph = collections.defaultdict(set)
        self.visited = set()
        self.ans = []

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        if endWord not in wordList:
            return []

        for word in wordList:
            for i in range(len(word)):
                self.graph[word[:i] + "*" + word[i + 1:]].add(word)

        self.endWord = endWord
        self.visited = {beginWord}

        self.dfs(beginWord, [beginWord])

        return self.ans

    def dfs(self, now, path):
        if self.ans:
            return
        if now == self.endWord:
            self.ans = list(path)
            return
        for i in range(len(now)):
            for near in self.graph[now[:i] + "*" + now[i + 1:]]:
                if near not in self.visited:
                    self.visited.add(near)
                    path.append(near)
                    self.dfs(near, path)
                    path.pop()


if __name__ == "__main__":
    # ["hit","hot","dot","lot","log","cog"]
    print(Solution().findLadders(beginWord="hit",
                                 endWord="cog",
                                 wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

    # []
    print(Solution().findLadders(beginWord="hit",
                                 endWord="cog",
                                 wordList=["hot", "dot", "dog", "lot", "log"]))
