# LeetCode题解(1679)：K和数对的最大数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-number-of-k-sum-pairs/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 124ms (91.48%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = collections.Counter([num for num in nums if num < k])

        ans = count[0] // 2

        for n1 in count:
            if n1 * 2 == k:
                ans += count[n1] // 2
            else:
                if k - n1 in count:
                    ans += min(count[n1], count[k - n1])
                    count[n1] = 0

        return ans
```

