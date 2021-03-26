from typing import List


class Word:
    __slots__ = "name", "near", "distance", "paths"

    def __init__(self, name):
        self.name = name
        self.near = set()  # 邻边列表
        self.distance = float("inf")  # 距离
        self.paths = []  # 路径


class Solution:
    def __init__(self):
        self.N = 0  # 单词长度
        self.words = {}  # 图的结点

    def check_transform(self, str1, str2):
        """比较两个单词是否可以通过一次转换获得"""
        differences = 0
        for i in range(self.N):
            if str1[i] != str2[i]:
                differences += 1
                if differences >= 2:
                    return False
        return differences == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.N = len(beginWord)  # 单词长度

        # 处理目标词不存在于词典的情况
        if endWord not in wordList:
            return []

        # 将开始词添加到无向图中
        wordList.append(beginWord)

        # 构造无向图中的结点
        for word in wordList:
            self.words[word] = Word(word)

        # 构造无向图中的边
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                word1 = wordList[i]
                word2 = wordList[j]
                if self.check_transform(wordList[i], wordList[j]):
                    self.words[word1].near.add(self.words[word2])
                    self.words[word2].near.add(self.words[word1])

        # 将开始词的距离和路径
        self.words[beginWord].distance = 0
        self.words[beginWord].paths = [[beginWord]]

        now_words = [beginWord]
        while now_words:
            has_find_end = False
            next_words = set()
            for name in now_words:
                node = self.words[name]  # 结点
                now_distance = node.distance
                now_paths = node.paths
                for near in node.near:
                    if near.name == endWord:
                        has_find_end = True
                    if near.distance >= now_distance + 1:
                        if near.distance > now_distance + 1:
                            near.paths = []
                        near.distance = now_distance + 1
                        for now_path in now_paths:
                            near.paths.append(now_path + [near.name])
                        next_words.add(near.name)

            now_words = list(next_words)

            if has_find_end:
                break

        return self.words[endWord].paths


if __name__ == "__main__":
    # [
    #   ["hit","hot","dot","dog","cog"],
    #   ["hit","hot","lot","log","cog"]
    # ]
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

    # []
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))

    # []
    print(Solution().findLadders(beginWord="hot", endWord="cog", wordList=["hot", "dog"]))

    # [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
    print(Solution().findLadders(beginWord="red", endWord="tax", wordList=["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
