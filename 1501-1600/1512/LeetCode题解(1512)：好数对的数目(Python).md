# LeetCode题解(1512)：好数对的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-good-pairs/)（简单）

标签：哈希表、数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (99.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter()
        ans = 0
        for n in nums:
            ans += count[n]
            count[n] += 1
        return ans
```