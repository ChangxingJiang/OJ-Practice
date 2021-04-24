# LeetCode题解(1785)：构成特定和需要添加的最少元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-elements-to-add-to-form-a-given-sum/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 62ms (93.97%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(sum(nums) - goal)

        if diff == 0:
            return 0
        else:
            return math.ceil(diff / limit)
```

