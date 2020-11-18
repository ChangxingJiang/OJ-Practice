# LeetCode题解(0140)：依据词典计算所有可能的单词拆分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-break-ii/)（困难）

标签：动态规划、回溯算法、记忆化递归

| 解法           | 时间复杂度                   | 空间复杂度               | 执行用时     |
| -------------- | ---------------------------- | ------------------------ | ------------ |
| Ans 1 (Python) | $O(2^N)$ : 其中N为字符串长度 | $O(D)$ : 其中D为字典词数 | 超出时间限制 |
| Ans 2 (Python) | $O(2^N)$                     | $O(D)$                   | 44ms (89%)   |
| Ans 3 (Python) |                              |                          |              |

解法一（回溯算法）：

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []

        word_set = set(wordDict)
        size = max(len(word) for word in word_set)

        def dfs(s1):
            ans = []

            if s1 in word_set:
                ans.append(s1)

            for i in range(1, len(s1)):
                if s1[:i] in word_set:
                    for s2 in dfs(s1[i:]):
                        ans.append(s1[:i] + " " + s2)
                if i > size:
                    break

            return ans

        return dfs(s)
```

解法二（记忆化递归）：

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []

        word_set = set(wordDict)
        size = max(len(word) for word in word_set)

        @functools.lru_cache(None)
        def dfs(s1):
            ans = []

            if s1 in word_set:
                ans.append(s1)

            for i in range(1, len(s1)):
                if s1[:i] in word_set:
                    for s2 in dfs(s1[i:]):
                        ans.append(s1[:i] + " " + s2)
                if i > size:
                    break

            return ans

        return dfs(s)
```



