# LeetCode题解(0777)：在LR字符串中交换相邻字符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/swap-adjacent-in-lr-string/)（中等）

标签：脑筋急转弯、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+N2)$ | 56ms (65.87%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # R只能往左、L只能往右
        lst1, lst2 = [], []
        for i, ch in enumerate(start):
            if ch != "X":
                lst1.append((i, ch))
        for i, ch in enumerate(end):
            if ch != "X":
                lst2.append((i, ch))

        if len(lst1) != len(lst2):
            return False

        size = len(lst1)

        for i in range(size):
            i1, ch1 = lst1[i]
            i2, ch2 = lst2[i]
            if ch1 != ch2:
                return False
            if ch1 == "L" and i1 < i2:
                return False
            if ch1 == "R" and i1 > i2:
                return False

        return True
```