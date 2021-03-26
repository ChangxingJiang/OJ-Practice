# LeetCode题解(面试16.16)：部分排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sub-sort-lcci/)（中等）

标签：数组、双指针、栈、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 84ms (98.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if len(array) < 2:
            return [-1, -1]

        stack, i2 = [], 0
        start = True
        max_val = float("-inf")
        for i, n in enumerate(array):
            # 计算开始位置
            while stack and n < stack[-1]:
                stack.pop()
                start = False
            if start:
                stack.append(n)

            # 计算结束位置
            if n >= max_val:
                max_val = n
            else:
                i2 = i

        return [len(stack), i2] if len(stack) < i2 else [-1, -1]
```