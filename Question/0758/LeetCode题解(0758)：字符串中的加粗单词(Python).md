# LeetCode题解(0758)：字符串中的加粗单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bold-words-in-string/)（简单）

标签：字符串、字典树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(W+S×L)$ | $O(W+S)$   | 48ms (92.52%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        # 构造字典树
        tree = {}
        for word in words:
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = ""

        # 使用字典树
        lst = [False] * len(S)
        for i in range(len(S)):
            m = i
            n = -1
            node = tree
            while m < len(S) and S[m] in node:
                node = node[S[m]]
                if "@" in node:
                    n = m
                m += 1

            if n != -1:
                for j in range(i, n + 1):
                    lst[j] = True

        ans = []

        for i in range(len(S)):
            if lst[i] is True and (i == 0 or lst[i - 1] is False):
                ans.append("<b>")
            ans.append(S[i])
            if lst[i] is True and (i == len(S) - 1 or lst[i + 1] is False):
                ans.append("</b>")

        return "".join(ans)
```