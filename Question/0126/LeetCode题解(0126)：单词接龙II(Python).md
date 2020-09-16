# LeetCode题解(0126)：依据单词列表玩单词接龙(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-ladder-ii/)（困难）

标签：字符串、广度优先遍历、回溯算法、图、图-无向图

| 解法           | 时间复杂度                                        | 空间复杂度                                        | 执行用时        |
| -------------- | ------------------------------------------------- | ------------------------------------------------- | --------------- |
| Ans 1 (Python) | $O(L^{N×C})$ : 其中L为最短路径长度，C为字符串长度 | $O(L^{N×C})$ : 其中L为最短路径长度，C为字符串长度 | 超出时间限制    |
| Ans 2 (Python) | $O(N^2×C)$ : 其中C为字符串长度                    | $O(N^2×C)$ : 其中C为字符串长度                    | 超出时间限制    |
| Ans 3 (Python) | $O(N×C×26)$                                       | $O(N×C)$                                          | 2128ms (11.54%) |
| Ans 3 (Python) | $O(N×C)$                                          | $O(N×C×26)$                                       | 300ms (55.87%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（朴素的广度优先遍历）：

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        N = len(beginWord)

        # 比较两个字符串是否可以通过一次转换获得
        def check_transform(str1, str2):
            differences = 0
            for i in range(N):
                if str1[i] != str2[i]:
                    differences += 1
                    if differences >= 2:
                        return False
            return differences == 1

        # 处理目标词不存在于词典的情况
        if endWord not in wordList:
            return []

        visited = set()
        now_paths = [(beginWord,)]  # 当前路径
        ans = []
        while now_paths:
            now_visited = set()
            next_paths = []
            for path in now_paths:
                now = path[-1]
                for word in wordList:
                    if word not in visited and check_transform(now, word):
                        if word == endWord:
                            ans.append(list(path + (word,)))
                        else:
                            now_visited.add(word)
                            next_paths.append(path + (word,))
            now_paths = next_paths
            visited.update(now_visited)
            if ans:
                break
        return ans
```

解法二（无向图的广度优先搜索）：

> 构造无向图的时间复杂度：$O(N^2×C)$
>
> 遍历的时间复杂度：$O(N^2)$

```python
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
```

解法三（集合用于记录当前节点）：

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        N = len(beginWord)  # 单词长度
        word_set = set(wordList)  # 单词集合

        # 处理目标词不存在于词典的情况
        if endWord not in wordList:
            return []

        # 寻找所有相邻结点
        def near(word):
            near_words = []
            arr = list(word)
            for i in range(N):  # 逐个字符遍历
                ch = arr[i]
                for code in range(97, 123):  # 每个字符遍历替换所有字母
                    arr[i] = chr(code)
                    new_word = "".join(arr)
                    if new_word in word_set and new_word not in marked:
                        near_words.append(new_word)
                arr[i] = ch
            return near_words

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

            if has_find_aim:  # 判断是否已经找到目标词
                break

        return ans
```

解法四（优化解法三计算邻边的方法）：

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        N = len(beginWord)  # 单词长度
        word_set = set(wordList)  # 单词集合

        # 处理目标词不存在于词典的情况
        if endWord not in wordList:
            return []

        # 初始化单词列表：将单词列表中每个单词的每个字符都替换为*，用以在O(C)的时间复杂度内计算邻边
        # 当前步骤时间复杂度：N×C
        word_hash = collections.defaultdict(list)
        for word in wordList:
            for i in range(N):
                word_hash[word[:i] + "*" + word[i + 1:]].append(word)

        # 寻找所有相邻结点
        def near(word):
            near_words = []
            for i in range(N):  # 逐个字符遍历
                for new_word in word_hash[word[:i] + "*" + word[i + 1:]]:
                    if new_word in word_set and new_word not in marked:
                        near_words.append(new_word)
            return near_words

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

            if has_find_aim:  # 判断是否已经找到目标词
                break

        return ans
```