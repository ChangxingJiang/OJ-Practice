# LeetCode题解(1646)：获取生成数组中的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/get-maximum-in-generated-array/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (12.93%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        lst = [-1] * (n + 1)

        for i in range(n + 1):
            if i == 0:
                lst[i] = 0
            elif i == 1:
                lst[i] = 1

            elif i % 2 == 0:
                lst[i] = lst[i // 2]
            else:
                lst[i] = lst[i // 2] + lst[i // 2 + 1]

        return max(lst)
```

