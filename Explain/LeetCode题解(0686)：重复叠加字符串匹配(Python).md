# LeetCode题解(0686)：判断字符串是否由另一个字符串叠加组成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/repeated-string-match/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度     | 执行用时       |
| -------------- | ---------- | -------------- | -------------- |
| Ans 1 (Python) | $O(N^2)$ | $O(N)$  |     108ms (83.43%)           |
| Ans 2 (Python) | $O(N)$   | $O(N)$         | 32ms (100.00%) |
| Ans 3 (Python) |            |                |                |

解法一（暴力解法）：

```python
def repeatedStringMatch(self, A: str, B: str) -> int:
    times = len(B) // len(A) + 2
    n = A * times
    if B in n:
        n = A * (times - 1)
        if B in n:
            n = A * (times - 2)
            if B in n:
                return times - 2
            else:
                return times - 1
        else:
            return times
    else:
        return -1
```

解法二（增加前置判断）：

![LeetCode题解(0686)：截图1.png](LeetCode题解(0686)：截图1.png)

```python
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if not set(B).issubset(set(A)):
            return -1
        size = len(B) // len(A)
        for i in range(size, size + 3):
            if B in A * i:
                return i
        return -1
```