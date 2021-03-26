# LeetCode题解(0648)：单词替换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/replace-words/)（中等）

标签：字典树、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $(D+S)$    | $O(D)$     | 56ms (97.96%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（字典树）：

```python
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {}

        for word in dictionary:
            now = root
            for ch in word:
                if ch not in now:
                    now[ch] = {}
                now = now[ch]
            now["@"] = None

        def replace(w):
            n = root
            for i, c in enumerate(w):
                if "@" in n:
                    return w[:i]
                if c not in n:
                    return w
                else:
                    n = n[c]
            return w

        return " ".join(replace(word) for word in sentence.split(" "))
```