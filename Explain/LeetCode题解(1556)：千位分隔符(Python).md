# LeetCode题解(1556)：在整数中添加千位分隔符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/thousand-separator/)（简单）

标签：数学、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 32ms (95.60%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = []
        while True:
            if n >= 1000:
                a, b = divmod(n, 1000)
                ans.append(str(b).zfill(3))
                n = a
            else:
                ans.append(str(n))
                break
        return ".".join(ans[::-1])
```