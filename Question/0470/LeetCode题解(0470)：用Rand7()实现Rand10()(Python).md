# LeetCode题解(0470)：用Rand7()实现Rand10()(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-rand10-using-rand7/)（中等）

标签：随机、拒绝采样

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | 期望 = $O(1)$ | $O(1)$     | 316ms (89.16%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def rand10(self):
        idx = 50
        while idx >= 40:
            i1, i2 = rand7(), rand7()
            idx = (i1 - 1) * 7 + i2 - 1
        return idx % 10 + 1
```