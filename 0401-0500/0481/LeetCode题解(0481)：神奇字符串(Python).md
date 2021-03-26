# LeetCode题解(0481)：神奇字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/magical-string/)（中等）

标签：双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 172ms (54.37%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        array = [1, 2, 2]
        i, now = 2, 1
        while len(array) < n:
            array.extend([now] * min(array[i], n - len(array)))
            i += 1
            now = 3 - now  # 1和2交换
        return array.count(1)
```

