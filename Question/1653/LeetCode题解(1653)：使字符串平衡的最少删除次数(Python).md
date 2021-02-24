# LeetCode题解(1653)：使字符串平衡的最少删除次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced/)（中等）

标签：贪心算法、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1392ms (34.69%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        size = len(s)

        lst1 = [0] * (size + 1)  # 左侧b的数量
        lst2 = [0] * (size + 1)  # 右侧a的数量

        for i in range(size):
            if s[i] == "b":
                lst1[i + 1] = lst1[i] + 1
            else:
                lst1[i + 1] = lst1[i]

        for i in range(size - 1, -1, -1):
            if s[i] == "a":
                lst2[i] = lst2[i + 1] + 1
            else:
                lst2[i] = lst2[i + 1]

        ans = size
        for i in range(size + 1):
            ans = min(ans, lst1[i] + lst2[i])
        return ans
```

