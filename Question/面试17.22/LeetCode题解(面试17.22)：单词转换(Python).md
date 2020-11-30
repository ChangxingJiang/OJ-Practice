# LeetCode题解(面试17.22)：单词转换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-transformer-lcci/)（中等）

标签：广度优先搜索、深度优先搜索、数组、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(W^2)$   | $O(W^2)$   | 超出时间限制   |
| Ans 2 (Python) | $O(W^2)$   | $O(W^2)$   | 超出时间限制   |
| Ans 3 (Python) | $O(W×L)$   | $O(W×L)$   | 124ms (88.80%) |

解法一（广度优先搜索）：

```python
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
```

解法二（深度优先搜索）：

```python
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

        def dfs(word, path):
            if word == endWord:
                return path
            for near in graph[word]:
                if near not in visited:
                    visited.add(near)
                    path.append(near)
                    res = dfs(near, path)
                    if res is not None:
                        return res
                    path.pop()
            return None

        return dfs(beginWord, [beginWord])
```

解法三：

```python
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
```

