# LeetCode题解(1437)：是否所有1都至少相隔k个元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (93.63%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1
        for i, n in enumerate(nums):
            if n == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        return True
```

