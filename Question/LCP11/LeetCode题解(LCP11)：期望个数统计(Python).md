# LeetCode题解(LCP11)：期望个数统计(Python)

题目：[原题链接](https://leetcode-cn.com/problems/qi-wang-ge-shu-tong-ji/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (76.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))
```