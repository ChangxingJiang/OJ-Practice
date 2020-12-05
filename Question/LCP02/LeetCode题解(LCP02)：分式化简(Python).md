# LeetCode题解(LCP02)：分式化简(Python)

题目：[原题链接](https://leetcode-cn.com/problems/deep-dark-fraction/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (82.12%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n1, n2 = cont.pop(), 1

        while cont:
            n1, n2 = n2, n1
            n1 += n2 * cont.pop()

        return [n1, n2]
```