# LeetCode题解(面试17.15)：最长单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-word-lcci/)（中等）

标签：字典树、递归、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(W+2^L)$ | $O(W+L)$   | 44ms (85.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)

        # 构造字典树
        tree = {}
        for word in words:
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = None

        # 判断是否由其他单词组成
        def is_consist(s, split=False):
            if split and s in word_set:
                return True

            n = tree
            for i, c in enumerate(s):
                if "@" in n and is_consist(s[i:], split=True):
                    return True
                if c in n:
                    n = n[c]
                else:
                    return False

            return False

        ans = sorted([word for word in words if is_consist(word)], key=lambda x: (-len(x), x))

        return ans[0] if ans else ""
```