# LeetCode题解(1065)：字符串的索引对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/index-pairs-of-a-string/)（简单）

标签：字符串、字典树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(W+T×L)$ | $O(W+T)$   | 48ms (79.59%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        tree = {}
        for i, word in enumerate(words):
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = i

        ans = []
        for i in range(len(text)):
            node = tree
            j = i
            while j < len(text) and text[j] in node:
                node = node[text[j]]
                if "@" in node:
                    ans.append([i, j])
                j += 1

        return ans
```