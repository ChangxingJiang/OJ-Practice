# LeetCode题解(1134)：阿姆斯特朗数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/armstrong-number/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 36ms (80.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isArmstrong(self, N: int) -> bool:
        lst = [int(ch) for ch in str(N)]
        ans = 0
        size = len(lst)
        for i in range(size):
            ans += lst[i] ** size
        return ans == N
```