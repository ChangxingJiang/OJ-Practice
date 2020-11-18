# LeetCode题解(面试08.06)：汉诺塔问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/hanota-lcci/)（简单）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (87.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        while A:
            B.append(A.pop())
        while B:
            C.append(B.pop())
```

