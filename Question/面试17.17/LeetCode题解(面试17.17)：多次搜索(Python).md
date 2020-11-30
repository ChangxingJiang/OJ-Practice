# LeetCode题解(面试17.17)：多次搜索(Python)

题目：[原题链接](https://leetcode-cn.com/problems/multi-search-lcci/)（中等）

标签：字典树、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(S+B)$   | $O(S+B)$   | 232ms (94.52%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        # 构造字典树
        tree = {}
        for i, word in enumerate(smalls):
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = i

        s1, s2 = len(smalls), len(big)

        ans = [[] for _ in range(s1)]

        for i in range(s2):
            j = i
            node = tree
            while j < s2 and big[j] in node:
                node = node[big[j]]
                j += 1
                if "@" in node:
                    ans[node["@"]].append(i)

        return ans
```