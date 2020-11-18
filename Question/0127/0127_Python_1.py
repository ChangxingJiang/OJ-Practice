import collections
from typing import List


# 广度优先搜索


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(beginWord)  # 单词长度
        word_set = set(wordList)  # 单词集合

        # 处理目标词不存在于词典的情况
        if endWord not in wordList:
            return 0

        # 初始化单词列表：将单词列表中每个单词的每个字符都替换为*，用以在O(C)的时间复杂度内计算邻边
        # 当前步骤时间复杂度：N×C
        word_hash = collections.defaultdict(list)
        for word in wordList:
            for i in range(N):
                word_hash[word[:i] + "*" + word[i + 1:]].append(word)

        # 寻找所有相邻结点
        def near(word):
            near_words = []
            for ii in range(N):  # 逐个字符遍历
                for new_word in word_hash[word[:ii] + "*" + word[ii + 1:]]:
                    if new_word in word_set and new_word not in marked:
                        near_words.append(new_word)
            return near_words

        step = 1

        marked = set()  # 已访问的节点
        queues = [[beginWord]]  # 当前路径
        ans = []

        while queues:
            new_queues = []  # 新的深度的路径
            has_find_aim = False  # 是否已找到目标词

            # 将上一个深度的结点加入到已访问的节点
            for queue in queues:
                marked.add(queue[-1])

            # 遍历寻找新的路径
            for queue in queues:
                for word in near(queue[-1]):
                    path = queue + [word]
                    if word == endWord:
                        ans.append(path)
                        has_find_aim = True
                    new_queues.append(path)

            queues = new_queues
            step += 1

            if has_find_aim:  # 判断是否已经找到目标词
                return step

        return 0


if __name__ == "__main__":
    # 5
    print(Solution().ladderLength(beginWord="hit",
                                  endWord="cog",
                                  wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

    # 0
    print(Solution().ladderLength(beginWord="hit",
                                  endWord="cog",
                                  wordList=["hot", "dot", "dog", "lot", "log"]))
