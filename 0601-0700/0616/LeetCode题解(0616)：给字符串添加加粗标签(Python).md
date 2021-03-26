# LeetCode题解(0616)：给字符串添加加粗标签(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-bold-tag-in-string/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2×W)$ | $O(N)$     | 140ms (75.81%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        size = len(s)
        mask = [False] * size
        for i in range(size):
            prefix = s[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, i + len(word)):
                        mask[j] = True

        ans = []
        last = False
        for i, ch in enumerate(s):
            if last == False and mask[i] == True:
                ans.append("<b>")
                last = True
            elif last == True and mask[i] == False:
                ans.append("</b>")
                last = False
            ans.append(ch)
        if last:
            ans.append("</b>")

        return "".join(ans)
```

