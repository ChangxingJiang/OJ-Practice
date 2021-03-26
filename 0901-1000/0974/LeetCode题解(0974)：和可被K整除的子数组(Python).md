# LeetCode题解(0974)：和可被K整除的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/)（中等）

标签：哈希表、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(K)$     | 356ms (83.96%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = collections.Counter({0: 1})

        ans = 0

        last = 0
        for n in A:
            last = (last + n) % K
            ans += count[last]
            count[last] += 1

        return ans
```