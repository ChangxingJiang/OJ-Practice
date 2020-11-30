# LeetCode题解(0560)：和为K的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subarray-sum-equals-k/)（中等）

标签：哈希表、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (8.70%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（前缀和）：

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = collections.Counter({0: 1})

        ans = 0

        last = 0
        for n in nums:
            last += n
            ans += hashmap[last - k]
            hashmap[last] += 1

        return ans
```