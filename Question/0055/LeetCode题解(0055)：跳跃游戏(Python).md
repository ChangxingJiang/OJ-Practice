# LeetCode题解(0055)：跳跃游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jump-game/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (72.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        now = 0
        for i in range(len(nums)):
            if now < i:
                return False
            now = max(now, i + nums[i])
            if now >= len(nums):
                return True
        return True
```

