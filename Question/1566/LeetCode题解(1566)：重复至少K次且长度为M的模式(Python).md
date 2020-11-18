# LeetCode题解(1566)：判断字符串中是否存在连续重复至少K次且长度为M的模式(Python)

题目：[原题链接](https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N×m×k)$ | $O(N)$     | 32ms (99%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            if arr[i:i + m * k] == arr[i:i + m] * k:
                return True
        return False
```