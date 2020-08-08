from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    # [
    #   ["hit","hot","dot","dog","cog"],
    #   ["hit","hot","lot","log","cog"]
    # ]
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

    # []
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
