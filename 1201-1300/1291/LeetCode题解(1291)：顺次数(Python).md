# LeetCode题解(1291)：顺次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sequential-digits/)（中等）

标签：数组、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 28ms (98.59%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
nums = []
for i in range(2, 10):
    v1 = int("".join([str(j) for j in range(1, i + 1)]))
    v2 = int("1" * i)
    nums.append(v1)
    for _ in range(9 - i):
        v1 += v2
        nums.append(v1)


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [num for num in nums if low <= num <= high]
```

