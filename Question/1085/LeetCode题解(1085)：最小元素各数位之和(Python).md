# LeetCode题解(1085)：最小元素各数位之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (94.68%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        ans = float("inf")
        for n in A:
            ans = min(ans, n)
        return 1 if sum(int(ch) for ch in str(ans)) % 2 == 0 else 0
```