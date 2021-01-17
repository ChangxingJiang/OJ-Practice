# LeetCode题解(0523)：连续的子数组和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/continuous-subarray-sum/)（中等）

标签：哈希表、动态规划、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (49.54%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visited = {0: -1}
        last = 0
        for i, num in enumerate(nums):
            last += num
            if k != 0:
                last %= k
            if last not in visited:
                visited[last] = i
            elif i - visited[last] > 1:
                return True
        return False
```

